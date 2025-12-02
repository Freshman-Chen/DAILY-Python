def extract_birthday_from_id(id_card):
    """
    从身份证号码中提取出生年月日
    
    参数:
        id_card (str): 身份证号码
    
    返回:
        dict: 包含年、月、日信息的字典
    """
    # 验证身份证号码长度（15位或18位）
    if len(id_card) not in [15, 18]:
        return {"error": "身份证号码长度不正确（应为15位或18位）"}
    
    try:
        # 根据身份证位数提取出生日期部分
        if len(id_card) == 15:
            # 15位身份证：7-12位为出生年月日（YYMMDD）
            birthday_str = id_card[6:12]
            year = "19" + birthday_str[0:2]  # 15位身份证年份前加19
            month = birthday_str[2:4]
            day = birthday_str[4:6]
        else:
            # 18位身份证：7-14位为出生年月日（YYYYMMDD）
            birthday_str = id_card[6:14]
            year = birthday_str[0:4]
            month = birthday_str[4:6]
            day = birthday_str[6:8]
        
        # 验证提取的日期是否有效
        if not (year.isdigit() and month.isdigit() and day.isdigit()):
            return {"error": "身份证号码格式不正确"}
        
        # 返回结果
        return {
            "year": year,
            "month": month,
            "day": day,
            "birthday": f"{year}年{month}月{day}日",
            "birthday_dash": f"{year}-{month}-{day}"
        }
    
    except Exception as e:
        return {"error": f"处理身份证号码时出错: {str(e)}"}

def main():
    """
    主函数：获取用户输入并显示结果
    """
    print("=" * 50)
    print("身份证出生日期提取程序")
    print("=" * 50)
    
    while True:
        # 获取用户输入
        id_card = input("\n请输入您的身份证号码（输入q退出）: ").strip()
        
        # 检查是否退出
        if id_card.lower() == 'q':
            print("程序已退出，再见！")
            break
        
        # 提取出生日期
        result = extract_birthday_from_id(id_card)
        
        # 显示结果
        print("\n" + "-" * 30)
        if "error" in result:
            print(f"错误: {result['error']}")
        else:
            print(f"身份证号码: {id_card}")
            print(f"出生年份: {result['year']}年")
            print(f"出生月份: {result['month']}月")
            print(f"出生日期: {result['day']}日")
            print(f"完整生日: {result['birthday']}")
            print(f"标准格式: {result['birthday_dash']}")
        print("-" * 30)

if __name__ == "__main__":    
    # 运行主程序
    print("\n" + "=" * 50)
    main()
