#coding:utf-8
"""
综合项目:世行历史数据基本分类及其可视化
作者：吴江
日期：2020.06.17
"""

import csv
import math
import pygal
import pygal_maps_world  #导入需要使用的库


def read_csv_as_nested_dict(filename, keyfield, separator, quote): #读取原始csv文件的数据，格式为嵌套字典
    
    result={}
    with open(filename,newline="") as csvfile:
        csvreader = csv.DictReader(csvfile,delimiter=separator,quotechar=quote)
        for row in csvreader:
            rowid = row[keyfield]
            result[rowid] = row

    return result


pygal_countries = pygal.maps.world.COUNTRIES #读取pygal.maps.world中国家代码信息（为字典格式），其中键为pygal中各国代码，值为对应的具体国名(建议将其显示在屏幕上了解具体格式和数据内容）
print(pygal_countries)


def reconcile_countries_by_name(plot_countries, gdp_countries): #返回在世行有GDP数据的绘图库国家代码字典，以及没有世行GDP数据的国家代码集合
    
    data = {}
    code = set()
    for key in plot_countries:
        for value in gdp_countries.values():
            if plot_countries[key] == value["Country Name"]:
                for year in range(1960, 2016):
                    if value[str(year)] != "":  #将在世行有GDP数据的绘图库国家信息加入字典
                        data[key] = value
                    else:
                        continue
    for CODE in plot_countries: #将在世行无GDP数据的绘图库国家代码加入集合
        if CODE not in data:
            code.add(CODE)
    tup = (data,code)
    return tup




def build_map_dict_by_name(gdpinfo, plot_countries, year):
    
    dict = {}
    Set = set()
    tup = reconcile_countries_by_name(plot_countries, read_csv_as_nested_dict("isp_gdp.csv", "Country Code", ",", '"'))
    with open(gdpinfo["gdpfile"], "rt") as csvfile:
        reade = csv.DictReader(csvfile, delimiter=gdpinfo["separator"], quotechar=gdpinfo["quote"])
        for cow in reade:
            for code in plot_countries:
                country = plot_countries[code]
                if country == cow[gdpinfo["country_name"]] and cow[year] != "":
                    dict[code] = math.log10(float(cow[year]))  # 该年有记录的加入字典
                elif country == cow[gdpinfo["country_name"]] and cow[year] == "":
                    Set.add(code)  # 该年无GDP记录的国家
                else:
                    continue
    set1 = tup[1]  # 完全没有GDP记录的国家代码
    set2 = Set - set1  # 没有某特定年记录的国家
    tup1 = (dict, set1, set2)
    return tup1



def render_world_map(gdpinfo, plot_countries, year, map_file): #将具体某年世界各国的GDP数据(包括缺少GDP数据以及只是在该年缺少GDP数据的国家)以地图形式可视化
    
    worldmap_chart = pygal.maps.world.World()
    worldmap_chart.title = "全球GDP分布图"  # 标题
    worldmap_chart.add(year, build_map_dict_by_name(gdpinfo, plot_countries, year)[0])  # 有GDP的国家画图
    worldmap_chart.add("missing from world bank",
                       build_map_dict_by_name(gdpinfo, plot_countries, year)[1])  # 完全没有GDP记录的国家图
    worldmap_chart.add("no data at this year",
                       build_map_dict_by_name(gdpinfo, plot_countries, year)[2])  # 没有某特定年记录的国家图
    worldmap_chart.render_to_file(map_file)  # 输出文件


def test_render_world_map(year):  #测试函数
    """
    对各功能函数进行测试
    """
    gdpinfo = {
        "gdpfile": "isp_gdp.csv",
        "separator": ",",
        "quote": '"',
        "min_year": 1960,
        "max_year": 2015,
        "country_name": "Country Name",
        "country_code": "Country Code"
    } #定义数据字典

    pygal_countries = pygal.maps.world.COUNTRIES  # 获得绘图库pygal国家代码字典
    render_world_map(gdpinfo, pygal_countries, year, "isp_gdp_world_name_%s.svg" % year)  # 调用函数



#程序测试和运行
print("欢迎使用世行GDP数据可视化查询")
print("----------------------")
year=input("请输入需查询的具体年份:")
test_render_world_map(year)
