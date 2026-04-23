from src.analysis import (
    FEATURE_COLUMNS,
    generate_demo_dataset,
    predict_activity,
    score_anomalies,
    summarize_segments,
    train_models,
)


def _sample_records(count: int = 8):
    dataset = generate_demo_dataset(samples=count, seed=7)
    return dataset[FEATURE_COLUMNS].to_dict(orient="records")


def test_train_and_predict_activity_outputs_expected_shape():
    dataset = generate_demo_dataset(samples=500, seed=99)
    artifacts = train_models(dataset, segment_count=4, seed=99)

    predictions = predict_activity(artifacts, _sample_records(12))

    assert len(predictions) == 12
    assert all("is_active" in row and "confidence" in row for row in predictions)
    assert 0.0 <= predictions[0]["confidence"] <= 1.0


def test_score_anomalies_is_bounded_between_zero_and_one():
    dataset = generate_demo_dataset(samples=700, seed=3)
    artifacts = train_models(dataset, segment_count=4, seed=3)

    scores = score_anomalies(artifacts, _sample_records(20))

    assert len(scores) == 20
    assert min(scores) >= 0.0
    assert max(scores) <= 1.0


def test_summarize_segments_returns_non_empty_counts():
    dataset = generate_demo_dataset(samples=600, seed=11)
    artifacts = train_models(dataset, segment_count=4, seed=11)

    summary = summarize_segments(artifacts, _sample_records(25))

    assert summary
    assert sum(summary.values()) == 25
