import mlflow
print("tracking the URi scheme below")
print(mlflow.get_tracking_uri())

print("\n")

mlflow.set_tracking_uri("http://127.0.0.1:5000")
print("tracking the  new URi scheme below")
print(mlflow.get_tracking_uri())