# === 순범안 비밀 암호 생성 및 해독 프로그램 ===

# 우리가 사용할 3가지 비밀 문자
CODE_WORDS = ['순', '범', '안']

def encode_to_sunbeoman(text):
    """일반 문장을 순범안 암호로 바꾸는 함수"""
    encoded_words = []
    
    for char in text:
        # 1. 글자를 컴퓨터 고유의 숫자(유니코드)로 변환
        num = ord(char)
        
        # 2. 숫자를 3진법(0, 1, 2)으로 변환
        if num == 0:
            base3 = '0'
        else:
            base3 = ''
            while num > 0:
                base3 = str(num % 3) + base3
                num //= 3
                
        # 3. 0, 1, 2를 각각 순, 범, 안으로 교체
        secret_word = ''.join(CODE_WORDS[int(digit)] for digit in base3)
        encoded_words.append(secret_word)
        
    # 글자 사이는 띄어쓰기로 구분해서 반환
    return ' '.join(encoded_words)

def decode_from_sunbeoman(secret_text):
    """순범안 암호를 다시 일반 문장으로 푸는 함수"""
    decoded_chars = []
    
    # 띄어쓰기를 기준으로 암호 덩어리들을 분리
    secret_words = secret_text.split(' ')
    
    for word in secret_words:
        if not word: 
            continue
            
        base3_str = ''
        for char in word:
            if char == '순':
                base3_str += '0'
            elif char == '범':
                base3_str += '1'
            elif char == '안':
                base3_str += '2'
            else:
                return "❌ 오류: '순', '범', '안' 이외의 글자가 섞여있거나 띄어쓰기가 잘못되었습니다."
                
        # 3진법 숫자를 다시 일반 숫자(10진수)로 변환 후 글자로 복구
        num = int(base3_str, 3)
        decoded_chars.append(chr(num))
        
    return ''.join(decoded_chars)

# === 실제 프로그램 실행 부분 ===
while True:
    print("\n" + "="*30)
    print(" 🕵️‍♂️ 순범안 비밀 암호 통신기 🕵️‍♀️")
    print("="*30)
    print("1. 일반 문장 -> 암호로 만들기")
    print("2. 암호 -> 일반 문장으로 해독하기")
    print("3. 프로그램 종료")
    
    choice = input("원하는 메뉴 번호를 입력하세요 (1/2/3): ")
    
    if choice == '1':
        user_input = input("\n암호로 바꿀 문장을 입력하세요:\n> ")
        result = encode_to_sunbeoman(user_input)
        print("\n[🔒 생성된 암호]")
        print(result)
        
    elif choice == '2':
        user_input = input("\n해독할 암호를 입력하세요 (띄어쓰기 포함):\n> ")
        result = decode_from_sunbeoman(user_input)
        print("\n[🔓 해독된 문장]")
        print(result)
        
    elif choice == '3':
        print("\n프로그램을 종료합니다.")
        break
        
    else:
        print("\n❌ 1, 2, 3 중에서 다시 입력해주세요.")
