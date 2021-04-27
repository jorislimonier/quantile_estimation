from quantile_estimation.data_prep import DataPrep
from quantile_estimation.data_visualization import DataVisualization
from quantile_estimation.bootstrap import Bootstrap

data_prep = DataPrep()
data_vis = DataVisualization()

results = data_prep.results
bs = Bootstrap()
boot = bs.bootstrap(bs.quantile(4), 500, results)
data_vis.hist_bootstrap(boot).show()