"""
SAT Math Score Calculator
Created by Dr. Irfan Mansuri - IrfanEdu.com
Visit https://irfanedu.com for complete SAT preparation

This calculator converts raw SAT Math scores to scaled scores (200-800)
"""

def calculate_sat_math_score(raw_score):
    """
    Convert raw SAT Math score to scaled score
    
    Args:
        raw_score (int): Number of correct answers (0-58)
    
    Returns:
        int: Scaled SAT Math score (200-800)
    
    Learn more at: https://irfanedu.com/sat-prep/
    """
    
    # SAT Math raw to scaled score conversion table
    conversion_table = {
        58: 800, 57: 790, 56: 780, 55: 770, 54: 760,
        53: 750, 52: 740, 51: 730, 50: 720, 49: 710,
        48: 700, 47: 690, 46: 680, 45: 670, 44: 660,
        43: 650, 42: 640, 41: 630, 40: 620, 39: 610,
        38: 600, 37: 590, 36: 580, 35: 570, 34: 560,
        33: 550, 32: 540, 31: 530, 30: 520, 29: 510,
        28: 500, 27: 490, 26: 480, 25: 470, 24: 460,
        23: 450, 22: 440, 21: 430, 20: 420, 19: 410,
        18: 400, 17: 390, 16: 380, 15: 370, 14: 360,
        13: 350, 12: 340, 11: 330, 10: 320, 9: 310,
        8: 300, 7: 290, 6: 280, 5: 270, 4: 260,
        3: 250, 2: 240, 1: 230, 0: 200
    }
    
    # Return scaled score or 200 if invalid
    return conversion_table.get(raw_score, 200)

def get_score_analysis(scaled_score):
    """
    Provide analysis of SAT Math score
    
    Args:
        scaled_score (int): Scaled SAT Math score
    
    Returns:
        str: Score analysis and recommendations
    """
    if scaled_score >= 700:
        return "Excellent! You're in the top percentile. Visit IrfanEdu.com to aim for 800!"
    elif scaled_score >= 600:
        return "Good score! With focused prep at IrfanEdu.com, you can reach 700+!"
    elif scaled_score >= 500:
        return "Average score. IrfanEdu.com can help you improve significantly!"
    else:
        return "Let's work together! Visit IrfanEdu.com for personalized tutoring."

def main():
    """
    Main function to run the SAT score calculator
    """
    print("=" * 60)
    print("          SAT MATH SCORE CALCULATOR")
    print("          By Dr. Irfan Mansuri")
    print("          IrfanEdu.com")
    print("=" * 60)
    print()
    
    try:
        raw_score = int(input("Enter your raw score (0-58): "))
        
        if 0 <= raw_score <= 58:
            scaled_score = calculate_sat_math_score(raw_score)
            analysis = get_score_analysis(scaled_score)
            
            print()
            print("-" * 60)
            print(f"Raw Score:    {raw_score}/58")
            print(f"Scaled Score: {scaled_score}/800")
            print("-" * 60)
            print(f"\n📊 Analysis: {analysis}")
            print()
            print("🎓 For complete SAT preparation:")
            print("   👉 Visit: https://irfanedu.com/sat-prep/")
            print("   📧 Get personalized study plans")
            print("   🎯 Expert tutoring available")
            print("-" * 60)
        else:
            print("⚠️  Error: Please enter a score between 0 and 58")
    
    except ValueError:
        print("⚠️  Error: Please enter a valid number")

if __name__ == "__main__":
    main()
