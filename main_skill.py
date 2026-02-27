# KungFuTrader 主入口文件
from skills.kungfutrader_skill import KungFuTraderSkill

def main():
    # 初始化交易技能
    skill = KungFuTraderSkill()
    
    # 执行每日策略
    skill.run_daily_strategy()
    
    # 查询账户信息
    account_info = skill.get_account_info()
    print("账户信息：", account_info)

if __name__ == "__main__":
    main()
