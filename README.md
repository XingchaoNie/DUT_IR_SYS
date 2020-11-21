# DUT_IR_SYS
DUT信息检索之搜索引擎
# DUT信息检索课程设计---搜索引擎
## GitHub链接：https://github.com/XingchaoNie/DUT_IR_SYS
## 语料库语料获取setSearchData.py
站点：http://sousuo.gov.cn/s.htm?t=zhengcelibrary&q=&p=

整个语料库来源共爬取网页2534个，获取语料31142条

为防止对目标服务器造成拥堵，设置了每次访问随机睡眠程序3~9秒

平均语料库数据获取共需要4~5小时

站点语料库更新有更多时，耗时随之变化

程序输出为CSV格式，信息详情可在文件内查看

本项目所有爬取内容均仅用于学习用途

## 语料库的搭建setMySQL.py
语料库使用MySql搭建

## 程序搜索主函数SearchMain.py
搜索引擎主函数，需在完成语料获取与语料库搭建后进行
