from zipline.pipeline import Pipeline
from pipeline_research.engine import ResearchPipelineEngine
from pipeline_research.assets.static import StaticAssetFinder

from pipeline_research.data.sources.nasdaq import list_symbols
from pipeline_research.data.nasdaq.factors import Sector
from pipeline_research.data.nasdaq.fundamentals import Company

# universe is all symbols located at nasdaq DataFrame
assetFinder = StaticAssetFinder(list_symbols)

eng = ResearchPipelineEngine(assetFinder)
pipe = Pipeline({
    'sector': Sector(),
    'name' : Company.name.latest,
    'sector_name' : Company.sector.latest
})#, screen=top5)

df = eng.run_pipeline(pipe, start_date='2019-01-02', end_date='2020-01-01')
print(df)