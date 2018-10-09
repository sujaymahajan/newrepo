import papermill as pm

pm.execute_notebook(
   'main.ipynb','main.ipynb',
   parameters = dict(alpha=0.6)
)