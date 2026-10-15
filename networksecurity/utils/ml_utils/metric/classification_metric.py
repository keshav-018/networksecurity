import sys
from networksecurity.entity.artifact_entity import ClassificationMetricArtifact
from networksecurity.exception.exception import NetworkSecurityException
from sklearn.metrics import precision_score, recall_score, f1_score

def get_classification_score(y_pred, y_true)->ClassificationMetricArtifact:
    try:
        model_f1_score = f1_score(y_pred, y_true)
        model_recall_score = recall_score(y_pred, y_true)
        model_precision_score = precision_score(y_pred, y_true)

        classification_metric = ClassificationMetricArtifact(
            f1_score=model_f1_score,
            precision_score=model_precision_score,
            recall_score=model_recall_score
        )
        return classification_metric
    except Exception as e:
        raise NetworkSecurityException(e, sys)