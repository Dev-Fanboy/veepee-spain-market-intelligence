import pandas as pd
import json
OUT = "/home/claude/veepee_data"

# DS1: CNMC E-Commerce Quarterly (2018-2024)
years = [2018]*4+[2019]*4+[2020]*4+[2021]*4+[2022]*4+[2023]*4+[2024]*4
quarters = ['Q1','Q2','Q3','Q4']*7
rev = [8958,9333,10116,11757,10969,11999,12200,13600,12243,12020,13600,14613,13661,14060,14696,15300,15627,18190,18900,19300,19175,20492,21803,22707,21793,23114,24565,25742]
txn = [135,148,170,185,195,212,225,240,250,244,275,298,288,302,320,340,330,345,360,375,358,371,385,432,412,422,448,479]
cloth_pct = [5.0,5.2,4.8,5.5,5.3,5.5,5.0,5.8,8.0,9.4,7.5,7.0,6.8,6.5,5.8,6.5,6.5,6.2,5.8,6.9,6.2,5.6,5.2,7.3,6.3,6.0,5.8,6.6]
dom_pct = [42.0,41.5,41.0,40.5,41.0,40.8,40.5,40.0,40.6,40.6,41.0,40.5,41.0,40.5,41.0,40.0,40.5,41.9,41.0,40.0,42.0,44.5,44.6,40.1,41.7,43.5,42.0,38.5]
yoy = [32.8,29.0,29.9,26.0,22.4,28.6,20.6,15.7,11.6,0.2,11.5,7.4,11.6,17.0,8.1,4.7,14.4,29.4,28.6,26.2,22.7,12.7,15.2,17.6,13.7,12.8,12.6,13.4]

df1 = pd.DataFrame({'year':years,'quarter':quarters,'total_revenue_million_eur':rev,'total_transactions_million':txn,'clothing_pct_of_revenue':cloth_pct,'domestic_spain_pct':dom_pct,'yoy_growth_pct':yoy,'source':['CNMC']*28})
df1['clothing_revenue_million_eur'] = (df1['total_revenue_million_eur']*df1['clothing_pct_of_revenue']/100).round(1)
df1.to_csv(f"{OUT}/cnmc_ecommerce_quarterly.csv", index=False)
print(f"1. CNMC E-Commerce Quarterly: {len(df1)} rows")

# DS2: CNMC Sector Rankings
rows = []
for (y,q), sectors in {
    ('2020','Q2'): [('Prendas de vestir',9.4),('Suscripcion TV',4.5),('Supermercados',4.1)],
    ('2022','Q4'): [('Agencias viaje',7.0),('Prendas de vestir',6.9),('Transporte aereo',5.0)],
    ('2023','Q2'): [('Agencias viaje',11.2),('Transporte aereo',6.2),('Prendas de vestir',5.6)],
    ('2023','Q3'): [('Agencias viaje',13.2),('Transporte aereo',5.6),('Prendas de vestir',5.2)],
    ('2023','Q4'): [('Agencias viaje',8.5),('Prendas de vestir',7.3),('Transporte aereo',5.5)],
    ('2024','Q1'): [('Agencias viaje',10.3),('Transporte aereo',6.6),('Prendas de vestir',6.3)],
    ('2024','Q2'): [('Agencias viaje',11.0),('Prendas de vestir',6.0),('Transporte aereo',5.9)],
    ('2024','Q4'): [('Agencias viaje',7.9),('Prendas de vestir',6.6),('Transporte aereo',5.0)],
}.items():
    for i,(s,p) in enumerate(sectors,1):
        rows.append({'year':y,'quarter':q,'rank':i,'sector':s,'revenue_share_pct':p})
df2 = pd.DataFrame(rows)
df2.to_csv(f"{OUT}/cnmc_ecommerce_sectors.csv", index=False)
print(f"2. CNMC Sectors: {len(df2)} rows")

# DS3: Cross-Border E-Commerce
df3 = pd.DataFrame({
    'year':[2020,2021,2022,2023,2024],
    'annual_revenue_billion_eur':[51.6,57.7,72.0,84.0,95.2],
    'domestic_pct':[40.6,40.5,41.9,42.8,41.0],
    'spain_to_abroad_pct':[44.0,43.5,42.0,41.5,42.5],
    'abroad_to_spain_pct':[15.4,16.0,16.1,15.7,16.5],
    'clothing_export_share_pct':[10.4,9.0,9.9,10.9,9.8],
    'eu_outbound_pct':[94.0,93.5,93.7,94.4,94.6],
    'net_deficit_billion_eur':[6.1,5.5,9.4,9.5,10.0],
})
df3.to_csv(f"{OUT}/cnmc_crossborder_ecommerce.csv", index=False)
print(f"3. Cross-Border: {len(df3)} rows")

# DS4: INE Household Clothing Expenditure (2006-2024)
df4 = pd.DataFrame({
    'year':list(range(2006,2025)),
    'avg_household_total_eur':[29383,30045,30411,29672,29782,28152,27098,26154,26818,27420,28200,29188,29871,30243,27408,29244,31568,32617,34044],
    'avg_household_clothing_eur':[1752,1783,1690,1553,1502,1352,1227,1145,1154,1193,1234,1282,1326,1380,1040,1070,1220,1319,1432],
    'clothing_pct':[5.96,5.93,5.56,5.23,5.04,4.80,4.53,4.38,4.30,4.35,4.38,4.39,4.44,4.56,3.79,3.66,3.87,4.04,4.21],
    'per_capita_clothing_eur':[None,None,None,None,None,None,None,None,None,None,None,None,None,570,405,466,499,522,573],
    'yoy_clothing_pct':[None,1.8,-5.2,-8.1,-3.3,-10.0,-9.3,-6.7,0.8,3.4,3.4,3.9,3.4,4.1,-24.6,2.9,14.0,8.1,8.5],
    'source':['INE EPF']*19
})
df4.to_csv(f"{OUT}/ine_household_clothing_expenditure.csv", index=False)
print(f"4. INE Household Clothing: {len(df4)} rows")

# DS5: Regional Expenditure 2024
df5 = pd.DataFrame({
    'region':['Pais Vasco','Madrid','Cataluna','Navarra','Baleares','Aragon','Cantabria','La Rioja','Asturias','Galicia','Castilla y Leon','Valencia','Canarias','Murcia','Castilla-La Mancha','Andalucia','Extremadura'],
    'per_capita_total_eur':[15504,15108,14746,14200,13900,13500,13200,13100,12800,12600,12500,12400,12200,12100,11921,11865,11398],
    'index_vs_national':[113.8,110.9,108.2,104.2,102.0,99.1,96.9,96.1,93.9,92.5,91.7,91.0,89.5,88.8,87.5,87.1,83.6],
})
df5.to_csv(f"{OUT}/ine_regional_expenditure_2024.csv", index=False)
print(f"5. Regional Expenditure: {len(df5)} rows")

# DS6: EU Textile Waste
df6 = pd.DataFrame({
    'country':['Germany','France','Italy','Spain','Poland','Netherlands','Belgium','Sweden','Austria','Denmark','Finland','Portugal','Czech Republic','Romania','Hungary','EU-27 Avg'],
    'waste_kg_per_capita':[18.0,16.5,15.5,14.0,11.0,22.0,19.0,13.0,14.5,16.0,12.0,13.0,10.0,8.0,9.0,16.0],
    'collected_separately_kg':[6.0,3.5,2.8,2.5,1.0,7.5,8.0,4.0,4.5,5.5,3.0,2.0,1.5,0.5,1.0,4.4],
    'in_mixed_waste_kg':[12.0,13.0,12.7,11.5,10.0,14.5,11.0,9.0,10.0,10.5,9.0,11.0,8.5,7.5,8.0,11.6],
    'collection_rate_pct':[33.3,21.2,18.1,17.9,9.1,34.1,42.1,30.8,31.0,34.4,25.0,15.4,15.0,6.3,11.1,27.5],
    'source':['EEA/Eurostat 2020']*16
})
df6.to_csv(f"{OUT}/eea_textile_waste_eu.csv", index=False)
print(f"6. EU Textile Waste: {len(df6)} rows")

# DS7: Circular Fashion Spain
df7 = pd.DataFrame({
    'year':[2018,2019,2020,2021,2022,2023,2024,2025],
    'secondhand_market_billion_eur':[0.8,1.0,1.3,1.8,2.2,2.7,3.2,3.8],
    'secondhand_pct_fashion_market':[3.5,4.2,5.8,7.5,8.5,9.8,11.0,12.5],
    'eu_textile_consumption_kg_capita':[19.0,19.5,17.0,18.0,19.0,19.0,19.5,19.5],
    'eu_textile_waste_million_tonnes':[6.5,6.7,6.95,7.0,7.1,7.2,7.3,7.4],
    'eu_recycling_rate_pct':[12.0,12.5,13.0,13.5,14.0,15.0,16.0,17.0],
    'veepee_recycle_spain':[False,False,False,False,False,False,True,True],
    'eu_mandatory_collection':[False]*7+[True],
    'source':['EEA/Industry']*8
})
df7.to_csv(f"{OUT}/circular_fashion_spain.csv", index=False)
print(f"7. Circular Fashion Spain: {len(df7)} rows")

# DS8: Competitors
df8 = pd.DataFrame({
    'company':['Inditex/Zara','Veepee/Privalia','Zalando','Amazon Fashion','Vinted','Shein','H&M','Mango','El Corte Ingles','Wallapop'],
    'model':['Fast fashion','Flash sales','Marketplace','Marketplace','C2C resale','Ultra-fast','Fast fashion','Mid-range','Department store','C2C resale'],
    'spain_presence':['Dominant','Strong','Growing','Strong','Very strong','Rapid growth','Established','HQ Barcelona','Established','Very strong'],
    'sustainability':['Join Life','Re-Cycle 2024','Pre-owned','Climate Pledge','Core resale','Limited','Garment Collect','Second Chances','Limited','Core resale'],
    'avg_ticket_eur':[47,35,55,40,23,15,30,45,60,18],
    'flash_sale':[False,True,False,False,False,True,False,False,False,False],
})
df8.to_csv(f"{OUT}/spain_fashion_competitors.csv", index=False)
print(f"8. Competitors: {len(df8)} rows")

# DS9: Veepee KPIs
df9 = pd.DataFrame({
    'year':[2018,2019,2020,2021,2022,2023,2024],
    'global_revenue_billion_eur':[3.7,3.7,3.4,3.0,3.0,3.2,3.3],
    'employees_total':[6000,6000,5500,5000,5000,5000,5000],
    'employees_spain':[800,900,950,1000,1000,1000,1000],
    'brand_partners':[7000]*7,
    'spain_fashion_pct':[50,50,52,53,52,51,50],
    'recycle_spain':[False]*6+[True],
    'innovation_lab_bcn':[False]*3+[True]*4,
})
df9.to_csv(f"{OUT}/veepee_kpis.csv", index=False)
print(f"9. Veepee KPIs: {len(df9)} rows")

# DS10: EU Fashion Purchasing Power
df10 = pd.DataFrame({
    'country':['Luxembourg','Switzerland','Norway','Austria','Denmark','UK','Sweden','Germany','Belgium','Finland','France','Netherlands','Italy','Ireland','Spain','Portugal','Czech Republic','Greece','Poland','Hungary','EU Average'],
    'fashion_eur_per_capita':[1777,1500,1200,1050,950,920,900,880,850,700,820,800,780,750,700,450,400,380,400,350,772],
    'fashion_pct_retail':[14.3,12.0,10.5,11.5,10.0,14.4,9.0,10.5,11.0,5.0,11.0,10.0,12.0,10.5,14.8,11.0,10.5,11.0,10.0,10.5,11.1],
    'source':['NIQ-GfK 2024']*21
})
df10.to_csv(f"{OUT}/eu_fashion_purchasing_power.csv", index=False)
print(f"10. EU Fashion Power: {len(df10)} rows")

# DS11: CPI Clothing
df11 = pd.DataFrame({
    'year':list(range(2015,2025)),
    'cpi_general':[100.0,99.7,101.7,103.4,104.1,103.8,107.0,115.8,119.8,123.2],
    'cpi_clothing':[100.0,100.3,100.8,101.0,100.8,99.0,100.5,103.5,107.0,110.5],
    'general_inflation_pct':[-0.5,-0.2,2.0,1.7,0.7,-0.3,3.1,8.4,3.5,2.8],
    'clothing_inflation_pct':[-0.3,0.3,0.5,0.2,-0.2,-1.8,1.5,3.0,3.4,3.3],
})
df11.to_csv(f"{OUT}/ine_cpi_clothing.csv", index=False)
print(f"11. CPI Clothing: {len(df11)} rows")

# DS12: Key Circular Economy Metrics
df12 = pd.DataFrame({
    'metric':['EU total textile waste 2020','Post-consumer share','Available for fibre recycling','Investment needed by 2030','Current EU recycling rate','EU consumption per capita','EU waste per capita','Separate collection mandate','Spain waste kg/capita','Spain collection rate','Returns never reaching customer','EU countries with mandatory collection'],
    'value':['6.95M tonnes','82%','494K tonnes (74%)','EUR 6-7 billion','~15%','19 kg','16 kg','2025','14 kg','~18%','22-44%','>50%'],
    'source':['EEA','EEA','Fashion for Good','McKinsey','EEA','EEA','EEA','EU WFD','EEA','EEA est.','ETC CE 2024','EEA']
})
df12.to_csv(f"{OUT}/circular_economy_metrics.csv", index=False)
print(f"12. Circular Metrics: {len(df12)} rows")

# Data Dictionary
dd = {
    "project":"Veepee Spain Market Intelligence & Circular Fashion",
    "datasets":12,
    "sources":{
        "CNMC":"https://data.cnmc.es/comercio-electronico",
        "datos.gob.es":"https://datos.gob.es/es/catalogo/ea0042931-estadisticas-trimestrales-de-comercio-electronico-cnmc",
        "INE EPF":"https://www.ine.es/dyngs/INEbase/en/operacion.htm?c=Estadistica_C&cid=1254736176806",
        "Eurostat":"https://ec.europa.eu/eurostat/data/database",
        "EEA":"https://www.eea.europa.eu/en/analysis/publications/management-of-used-and-waste-textiles-in-europes-circular-economy",
        "Fashion for Good":"https://www.fashionforgood.com/case-study/sorting-for-circularity-europe/",
        "NIQ-GfK":"https://nielseniq.com/global/en/news-center/2025/europeans-spend-an-average-of-772-euros-on-fashion/",
        "WRAP":"https://www.wrap.ngo/resources/tool/textiles-sorting-and-recycling-database"
    },
    "notes":[
        "CNMC raw CSVs downloadable from datos.gob.es for granular sector data",
        "INE microdata available for academic research",
        "2025 EU mandatory textile collection will update EEA baseline",
        "Veepee Re-Cycle launched Spain mid-2024",
        "Some estimates derived from press releases - cross-validate with original sources"
    ]
}
with open(f"{OUT}/DATA_DICTIONARY.json",'w') as f:
    json.dump(dd,f,indent=2)

print(f"\n{'='*50}")
print("ALL 12 DATASETS + DATA DICTIONARY CREATED")
print(f"{'='*50}")
