from mlflow.store.artifact.models_artifact_repo import ModelsArtifactRepository
from mlflow.tracking import MlflowClient

client = MlflowClient()
my_model = client.download_artifacts("f648803d1d1e44d4bbaf1f6ed13dd537", path="model", dst_path=".")
print(f"Placed model in: {my_model}")
