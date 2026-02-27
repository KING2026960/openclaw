# KungFuTrader 主入口文件
 from skills.kungfutrader_skill import KungFuTraderSkill
 def main():
     """
     主入口函数：初始化并启动KungFuTrader截拳道量化交易Agent
     """
     # 初始化交易智能体
     agent = KungFuTraderSkill(market="A股", broker="东方财富")
     
     # 执行每日量化策略
     agent.run_daily_strategy()
     
     # 查询账户信息
     account_info = agent.get_account_info()
     print("账户信息：", account_info)
 if __name__ == "__main__":
     main()
