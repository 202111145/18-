data=int(input("어서오세요, 무인카페 '코코다방'에 오신 것을 환영합니다! 취향 테스트 진행 후, 저희가 분석한 고객님의 취향에 맞는 커피 및 음료를 추천해드리겠습니다. 먼저 테스트를 진행할 언어를 선택해 주세요. 한국어는 1, 日本語는 2, English는 3을 입력해주세요. : "))


if data==1 :

    print("그럼, 테스트를 시작하도록 하겠습니다.")
    print()
    while True:
        a=int(input("Q1. 아침에 일어나 창문을 봤을 때, 어떤 하늘이 보였으면 하나요? - 따뜻한 봄날의 화창한 하늘(1), 햇빛쨍쨍 푸른 하늘(2), 비 내리는 흐린 하늘(3), 함박눈 내리는 겨울 하늘(4) : "))
        print()
        if 0<a<5:
            break
        else :
            print("1,2,3,4 중에서 입력해주세요.")
            continue

    while True:
        b=int(input("Q2. 어떤 디저트를 좋아하시나요? - 달다구리 마카롱(1), 매일 당기는 아이스크림(2), 담백한 휘낭시에(3), 디저트의 정석 케이크(4) : "))
        print()
        if 0<b<5:
            break
        else :
            print("1,2,3,4 중에서 입력해주세요.")
            continue
    

    while True:
        c=int(input("Q3. 자신의 방을 어떤 분위기의 방으로 꾸미고 싶은가요? - 따뜻하고 아늑한 분위기(1), 뒤죽박죽이어도 난 행복해(2), 인스타 감성 가득 미니멀 스타일(3), 깔끔, 모던한 분위기(4) : "))
        print()
        if 0<c<5:
            break   
        else :
            print("1,2,3,4 중에서 입력해주세요.")
            continue
    

    while True:
        d=int(input("Q4. 당신에게 일주일의 보상 휴가가 주어진다면 어떤 여행을 하고 싶나요? - 도시를 벗어나 탁 트인 산과 바다로(1), 문화유산을 보러 해외 관광 여행(2), 쉬는 만큼 찌는 식도락 여행(3), 우리 집 침대랑 방콕 여행(4) : "))
        print()
        if 0<d<5:
            break
        else :
            print("1,2,3,4 중에서 입력해주세요.")
            continue


    while True:
        e=int(input("Q5. 자신과 어울린다고 생각하는 색깔은 어느 것인가요? - 부드럽고 발랄한 파스텔 톤(1), 개성 있고 활동적인 원색(2), 시크하고 힙한 무채색(3), 난 다 잘 어울린다 ^_^(4) : "))
        print()
        if 0<e<5:
            break
        else :
            print("1,2,3,4 중에서 입력해주세요.")
            continue
    

    while True:
        f=int(input("Q6. 평소 자신이 즐겨입는 옷 스타일은 무엇인가요? - 러블리하고 귀여운 스타일(1), 편한 게 최고! 원마일룩(2), 간지철철 힙한 스타일(3), 깔끔 단정한 정장스타일(4) : "))
        print()
        if 0<f<5:
            break 
        else :
            print("1,2,3,4 중에서 입력해주세요.")
            continue


    while True:
        g=int(input("Q7. 상대방이 나를 어떤 향으로 기억했으면 하나요? (자주 쓰는, 좋아하는 향) - 화사한 플로럴 계열(1), 상큼한 시트러스 계열(2), 중성적이고 시크한 우디 계열(3), 파우더리하고 따뜻한 머스크 계열(4) : "))
        print()
        if 0<g<5:
            break
        else :
            print("1,2,3,4 중에서 입력해주세요.")
            continue


    while True:
        h=int(input("Q8. 쉬는 날, 자신만의 힐링 방법은 무엇인가요? - 친구랑 수다 떨며 놀기(1), 내 사전에 근손실은 없다. 운동하기(2), 어디로든 떠나 혼자만의 시간 보내기(3), 쉴 땐 푹 쉬어야지, 집콕(4) : "))
        print()
        print()
        if 0<g<5:
            print(" - 모든 테스트가 종료되었습니다. 결론을 도출 중 입니다... - ")
            print()
            print()
            break
        else :
            print("1,2,3,4 중에서 입력해주세요.")
            continue


    total=(a+b+c+d+e+f+g+h) 

    if 8 <=total<=11 :
        print("취향 테스트 결과에 따라, 당신처럼 새콤달콤한 꿀자몽티를 추천드립니다.")

    elif 12<=total<=15 :
        print("취향 테스트 결과에 따라, 당신처럼 톡톡튀는 매력을 가진 샹그리아 에이드를 추천드립니다.")

    elif 16<=total<=19 :
        print("취향 테스트 결과에 따라, 당신처럼 폭신폭신한 바닐라 라떼를 추천드립니다.")
    
    elif 20<=total<=23 :
        print("취향 테스트 결과에 따라, 매니아 층이 있는 말차 라떼를 추천드립니다.")

    elif 24<=total<=27 :
        print("취향 테스트 결과에 따라, 쌉싸름한 매력을 가진 얼그레이 라떼를 추천드립니다.")

    else:
        print("취향 테스트 결과에 따라, 샷 추가가 어울리는 당신에게 아메리카노를 추천드립니다.")




        
if data==2 :

    print("ではテストを開始します。")
    print()
    while True:
        a=int(input("Q1. 朝起きて窓を見た時、どんな空が見えたら良いですか？ - 暖かい春の日の晴れた空(1)、日差しの青い空(2)、雨の降る曇った空(3)、ハンバーグ雪の降る冬の空(4) :"))
        print()
        if 0<a<5:
            break
        else :
            print("1、2、3、4の中から入力してください。")
            continue


    while True:
        b=int(input("Q2. どんなデザートが好きですか？ - タルダクリマカロン(1)、毎日食べたいアイスクリーム(2)、さっぱりとしたフィナンシェ(3)、デザートの定番ケーキ(4) : "))
        print()
        if 0<b<5:
            break
        else :
            print("1、2、3、4の中から入力してください。")
            continue


    while True:
        c=int(input("Q3. 自分の部屋をどんな雰囲気の部屋にしたいですか？ - 暖かくて居心地の良い雰囲気(1)、ごちゃごちゃでも私は幸せ(2)、インスタグラムの感性いっぱいのミニマルスタイル(3)、すっきり、モダンな雰囲気(4) : "))
        print()
        if 0<c<5:
            break
        else :
            print("1、2、3、4の中から入力してください。")
            continue
    

    while True:
        d=int(input("Q4. 一週間の報酬休暇が与えられたら、どんな旅行をしたいですか？ - 都市を抜け出して広々とした山と海へ(1)、文化遺産を見に海外観光旅行(2)、休む分蒸すグルメ旅行(3)、我が家のベッドとバンコク旅行(4) : "))
        print()
        if 0<d<5:
            break
        else :
            print("1、2、3、4の中から入力してください。")
            continue



    while True:
        e=int(input("Q5. 自分に合うと思う色はどれですか？ - 柔らかくて溌剌としたパステルトーン(1)、個性的で活動的な原色(2)、シックでヒップな無彩色(3)、私は全部よく似合う ^_^(4) : "))
        print()
        if 0<e<5:
            break
        else :
            print("1、2、3、4の中から入力してください。")
            continue

    

    while True:
        f=int(input("Q6. 普段自分がよく着る服スタイルは何ですか? - ラブリ-と可愛いスタイル(1)、楽なのが最高!ワンマイル・ルック(2)、干支どくどくとヒプハンスタイル(3)、カルクム端正なスーツスタイル(4) : "))
        print()
        if 0<f<5:
            break
        else :
            print("1、2、3、4の中から入力してください。")
            continue


    while True:
        g=int(input("Q7. 相手に私をどんな香りで覚えてもらいたいですか？ (よく使う、好きな香り) - 華やかなフローラル系(1)、さわやかなシトラス系(2)、中性的でシックなウッディ系(3)、パウダリーで暖かいムスク系(4) : "))
        print()
        if 0<g<5:
            break
        else :
            print("1、2、3、4の中から入力してください。")
            continue


    while True:
        h=int(input("Q8. 休みの日、自分だけのヒーリング方法は何ですか？ - 友達とおしゃべりして遊ぶ(1)、私の辞書に根損失はない。 運動する(2)、どこへでも行って一人だけの時間を過ごす(3)、休む時はゆっくり休まないと、家の中(4) : "))
        print()
        print()
        if 0<g<5:
            print(" - すべてのテストが終了しました。 結論を導出中です... -")
            print()
            print()
            break
        else :
            print("1、2、3、4の中から入力してください。")
            continue



    total=(a+b+c+d+e+f+g+h) 

    if 8 <=total<=11 :
        print("好みテストの結果次第、あなたのように甘酸っぱい蜂蜜グレープフルーツティーをおすすめします。")

    elif 12<=total<=15 :
        print("好みテストの結果次第、あなたのように魅力的なシャングリアエードをお勧めします。")

    elif 16<=total<=19 :
        print("好みテストの結果次第、あなたのようにふわふわしたバニララテをお勧めします。")
    
    elif 20<=total<=23 :
        print("好みテストの結果次第、ほろ苦い魅力を持った抹茶ラテをおすすめします。")

    elif 24<=total<=27 :
        print("好みテストの結果次第、ほろ苦い魅力を持ったアールグレイラテをお勧めいたします。")

    elif 28<=total<=32 :
        print("好みテストの結果次第、ショットの追加が似合うあなたにアメリカーノをお勧めします。")





if data==3 :
    print("Then, let's start the test.")
    print()
    while True:
        a=int(input("Q1. When you wake up in the morning and look out the window, what kind of sky do you want to see? - Sunny sky in spring (1), on a warm spring day, sunny blue sky (2), cloudy sky on a rainy day (3), winter sky on a snowy day (4) :"))
        print()
        if 0<a<5:
            break
        else :
            print("Please enter it among 1, 2, 3, 4.")
            continue


    while True:
        b=int(input("Q2. What kind of dessert do you like? - Sweet macaron (1), ice cream (2), light financier (3), standard dessert cake (4) : "))
        print()
        if 0<b<5:
            break
        else :
            print("Please enter it among 1, 2, 3, 4.")
            continue


    while True:
        c=int(input("Q3. What kind of atmosphere do you want to decorate your room with? - Warm and cozy atmosphere (1), I'm happy even if it's mixed up (2), minimal style (3), neat and modern (4) : "))
        print()
        if 0<c<5:
            break
        else :
            print("Please enter it among 1, 2, 3, 4.")
            continue
    

    while True:
        d=int(input("Q4. What kind of trip would you like to take if you were given a week of compensation leave? - Out of the city, into the open mountains and seas (1), overseas sightseeing tours to see cultural heritage (2), a eating trip(piggy piggy) (3), a trip to my bed (bang-kok) (4) : "))
        print()
        if 0<d<5:
            break
        else :
            print("Please enter it among 1, 2, 3, 4.")
            continue


    while True:
        e=int(input("Q5. Which color do you think suits you? - Soft pastel tone (1), unique and active primary color (2), chic and hip color (3), I look good in everything. ^_^(4) : "))
        print()
        if 0<e<5:
            break
        else :
            print("Please enter it among 1, 2, 3, 4.")
            continue


    while True:
        f=int(input("Q6. What's your favorite fashion style? - Lovely and cute style (1), Comfortable is the best! One-mile look (2), neat hip style (3), neat suit style (4) : "))
        print()
        if 0<f<5:
            break
        else :
            print("Please enter it among 1, 2, 3, 4.")
            continue


    while True:
        g=int(input("Q7. What scent do you want the other person to remember me? (Frequently used, favorite scent) - Bright floral (1), fresh citrus (2), neutral and chic woody (3), powdery and warm musk (4) : "))
        print()
        if 0<g<5:
            break
        else :
            print("Please enter it among 1, 2, 3, 4.")
            continue


    while True:
        h=int(input("Q8. What is your own way of healing on your day off? - Chatting and playing with friends (1) There is no muscle loss in my life. Exercising (2), going anywhere and spending time alone (3), resting well & staying at home (4) : "))
        print()
        print()
        if 0<g<5:
            print(" - All tests have been completed. I'm drawing a conclusion. - ")
            print()
            print()
            break
        else :
            print("Please enter it among 1, 2, 3, 4.")
            continue



    total=(a+b+c+d+e+f+g+h) 

    if 8 <=total<=11 :
        print("Depending on the results of the taste test, I recommend sweet honey grapefruit tea like you.")

    elif 12<=total<=15 :
        print("Depending on the results of the taste test, I recommend Shangria Ade, which has a popping charm like you.")

    elif 16<=total<=19 :
        print("Depending on the results of the taste test, I recommend a soft vanilla latte like you.")
        
    elif 20<=total<=23 :
        print("Depending on the results of the taste test, I recommend addictive Malcha Latte.")

    elif 24<=total<=27 :
        print("Depending on the results of the taste test, I recommend Earl Grey Latte, which has a bitter charm.")

    elif 28<=total<=32 :
        print("Depending on the results of the taste test, I recommend Americano with additional shots.")

