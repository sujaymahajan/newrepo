import papermill as pm

pm.execute_notebook(
   'main.ipynb',
   parameters = dict(alpha=0.6, ratio=0.1)
)