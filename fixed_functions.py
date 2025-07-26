# ================================
# GRAMMAR AI FUNCTIONS - FIXED VERSION  
# ================================

def get_korean_grammar_explanation(user_input):
    """Kores grammar tushuntirish AI funksiyasi - Fixed"""
    input_text = user_input.lower()
    
    # Basic particles
    if any(word in input_text for word in ["은", "는", "eun", "neun", "mavzu", "subject"]):
        return """📚 <b>은/는 - Mavzu belgisi</b>

🔍 <b>Qoida:</b> Gapning mavzusini ko'rsatadi
💡 <b>Misollar:</b>
1. 저는 학생입니다 "Men talabaman"
2. 책은 재미있어요 "Kitob qiziqarli"
🎯 <b>Qoida:</b> Undosh + 은, Unli + 는"""

    elif any(word in input_text for word in ["이", "가", "i", "ga", "egalik"]):
        return """📚 <b>이/가 - Egalik belgisi</b>

🔍 <b>Qoida:</b> Gapning egasini aniq ko'rsatadi
💡 <b>Misollar:</b>
1. 고양이가 귀여워요 "Mushuk chiroyli"  
2. 사람이 많아요 "Odam ko'p"
🎯 <b>Qoida:</b> Undosh + 이, Unli + 가"""

    elif any(word in input_text for word in ["을", "를", "eul", "reul", "to'ldiruvchi"]):
        return """📚 <b>을/를 - To'ldiruvchi belgisi</b>

🔍 <b>Qoida:</b> Fe'lning to'ldiruvchisini ko'rsatadi
💡 <b>Misollar:</b> 
1. 사과를 먹어요 "Olma yeyapman"
2. 책을 읽어요 "Kitob o'qiyapman"
🎯 <b>Qoida:</b> Undosh + 을, Unli + 를"""

    # Location and direction
    elif any(word in input_text for word in ["에서", "eseo", "joy", "da", "dan"]):
        return """📚 <b>에서 - Joy belgisi</b>

🔍 <b>Qoida:</b> Harakat qilinadigan joyni ko'rsatadi
💡 <b>Misollar:</b>
1. 학교에서 공부해요 "Maktabda o'qiyapman"
2. 집에서 쉬어요 "Uyda dam olayapman" 
🎯 <b>Farq:</b> 에서 - harakat joyi, 에 - maqsad joyi"""

    elif any(word in input_text for word in ["에게", "ege", "kimga"]):
        return """📚 <b>에게 - "Kimga" belgisi</b>

🔍 <b>Qoida:</b> Insonlar uchun "kimga" ma'nosi
💡 <b>Misollar:</b>
1. 친구에게 편지를 써요 "Do'stga xat yozayapman"
2. 선생님에게 물어봐요 "O'qituvchidan so'rayapman"
🎯 <b>한테 = 에게</b> (norasmiy = rasmiy)"""

    # Time particles  
    elif any(word in input_text for word in ["부터", "buteo", "boshlab", "dan"]):
        return """📚 <b>부터 - "Dan boshlab"</b>

🔍 <b>Qoida:</b> Boshlanish nuqtasini ko'rsatadi
💡 <b>Misollar:</b>
1. 9시부터 일해요 "9 dan boshlab ishlayman"
2. 월요일부터 바빠요 "Dushanbadan boshlab bandman"
🎯 <b>까지 bilan:</b> 부터...까지 "dan...gacha" """

    elif any(word in input_text for word in ["까지", "kkaji", "gacha"]):
        return """📚 <b>까지 - "Gacha"</b>

🔍 <b>Qoida:</b> Tugash nuqtasini ko'rsatadi
💡 <b>Misollar:</b>
1. 5시까지 일해요 "5 gacha ishlayman"
2. 역까지 걸어가요 "Bekatgacha boraman"
🎯 <b>부터 bilan:</b> 부터...까지 "dan...gacha" """

    # Connecting particles
    elif any(word in input_text for word in ["와", "과", "wa", "gwa", "bilan"]):
        return """📚 <b>와/과 - "Bilan"</b>

🔍 <b>Qoida:</b> "Bilan" ma'nosida ishlatiladi  
💡 <b>Misollar:</b>
1. 친구와 영화를 봐요 "Do'st bilan kino ko'rayapman"
2. 가족과 여행해요 "Oila bilan sayohat qilaman"
🎯 <b>Qoida:</b> Unli + 와, Undosh + 과"""

    elif any(word in input_text for word in ["도", "do", "ham"]):
        return """📚 <b>도 - "Ham"</b>

🔍 <b>Qoida:</b> "Ham", "shuningdek" ma'nosi
💡 <b>Misollar:</b>
1. 저도 학생이에요 "Men ham talabaman"
2. 사과도 좋아해요 "Olma ham yoqadi"
🎯 <b>은/는, 이/가 o'rnida ishlatiladi</b>"""

    elif any(word in input_text for word in ["만", "man", "faqat"]):
        return """📚 <b>만 - "Faqat"</b>

🔍 <b>Qoida:</b> Cheklashni bildiradi
💡 <b>Misollar:</b>
1. 물만 마셔요 "Faqat suv ichaman"
2. 한국어만 공부해요 "Faqat koreys tilini o'rganaman"
🎯 <b>Boshqa belgilar bilan almashtiriladi</b>"""

    # Verb forms
    elif any(word in input_text for word in ["하다", "hada", "qilmoq"]):
        return """📚 <b>하다 - "Qilmoq" fe'li</b>

🔍 <b>Qoida:</b> Koreaning asosiy fe'li
💡 <b>Misollar:</b>
1. 공부하다 → 공부해요 "O'qimoq → O'qiyapman"
2. 운동하다 → 운동했어요 "Sport qilmoq → Sport qildim"
🎯 <b>Ko'p so'zlar bilan birikadi</b>"""

    # Formal present
    elif any(word in input_text for word in ["습니다", "seumnida", "rasmiy"]):
        return """📚 <b>습니다/ㅂ니다 - Rasmiy hozirgi</b>

🔍 <b>Qoida:</b> Eng rasmiy so'lash shakli
💡 <b>Misollar:</b>
1. 먹습니다 "Yeyapman" (rasmiy)
2. 갑니다 "Borayapman" (rasmiy)
🎯 <b>Undosh + 습니다, Unli + ㅂ니다</b>"""

    # Informal present  
    elif any(word in input_text for word in ["아요", "어요", "ayo", "eoyo", "norasmiy"]):
        return """📚 <b>아요/어요 - Norasmiy hozirgi</b>

🔍 <b>Qoida:</b> Kundalik suhbatda ishlatiladi
💡 <b>Misollar:</b>
1. 가요 "Borayapman"
2. 먹어요 "Yeyapman"
🎯 <b>A/O unli + 아요, boshqa + 어요</b>"""

    # Past tense
    elif any(word in input_text for word in ["었다", "eotda", "o'tgan"]):
        return """📚 <b>었다/았다 - O'tgan zamon</b>

🔍 <b>Qoida:</b> O'tgan zamondagi harakat
💡 <b>Misollar:</b>
1. 갔어요 "Bordim"
2. 먹었어요 "Yedim"
🎯 <b>A/O unli + 았, boshqa + 었</b>"""

    # Future tense
    elif any(word in input_text for word in ["겠다", "getda", "kelajak"]):
        return """📚 <b>겠다 - Kelajak zamon</b>

🔍 <b>Qoida:</b> Kelajakdagi reja va niyat
💡 <b>Misollar:</b>
1. 가겠어요 "Boraman"
2. 공부하겠습니다 "O'qiyman"
🎯 <b>Yumshoq vada va ehtimollik</b>"""

    # Connectors
    elif any(word in input_text for word in ["고", "go", "va", "keyin"]):
        return """📚 <b>고 - "Va" bog'lovchi</b>

🔍 <b>Qoida:</b> Ikki harakatni ketma-ket bog'laydi
💡 <b>Misollar:</b>
1. 집에 가고 쉬어요 "Uyga borib dam olaman"
2. 밥을 먹고 커피를 마셔요 "Ovqat yeyib kofe ichaman"
🎯 <b>Vaqt tartibini bildiradi</b>"""

    elif any(word in input_text for word in ["지만", "jiman", "lekin"]):
        return """📚 <b>지만 - "Lekin"</b>

🔍 <b>Qoida:</b> Qarama-qarshilikni bildiradi
💡 <b>Misollar:</b>
1. 비싸지만 좋아요 "Qimmat lekin yaxshi"
2. 어렵지만 재미있어요 "Qiyin lekin qiziqarli"
🎯 <b>Ziddiyatli fikrlarni bog'laydi</b>"""

    elif any(word in input_text for word in ["려고", "ryeogo", "maqsad", "moqchi"]):
        return """📚 <b>려고 하다 - Maqsad</b>

🔍 <b>Qoida:</b> Maqsad va niyatni bildiradi
💡 <b>Misollar:</b>
1. 한국에 가려고 해요 "Koreyaga bormoqchiman"
2. 공부하려고 해요 "O'qimoqchiman"
🎯 <b>Rejalar uchun ishlatiladi</b>"""

    # Advanced patterns
    elif any(word in input_text for word in ["는데", "neunde", "holat"]):
        return """📚 <b>는데 - Holat bildiruvchi</b>

🔍 <b>Qoida:</b> Holat va tushuntirishni bildiradi
💡 <b>Misollar:</b>
1. 비가 오는데 나갈까요? "Yomg'ir yog'yapti, chiqamizmi?"
2. 음식이 맛있는데 비싸요 "Taom mazali, lekin qimmat"
🎯 <b>Ma'lumot berish uchun</b>"""

    elif any(word in input_text for word in ["아도", "어도", "garchi"]):
        return """📚 <b>아도/어도 - "Garchi"</b>

🔍 <b>Qoida:</b> "Garchi...ham" ma'nosi
💡 <b>Misollar:</b>
1. 비가 와도 갈게요 "Yomg'ir yog'sa ham boraman"
2. 어려워도 할게요 "Qiyin bo'lsa ham qilaman"
🎯 <b>A/O unli + 아도, boshqa + 어도</b>"""

    elif any(word in input_text for word in ["거든요", "geodeunyo", "chunki"]):
        return """📚 <b>거든요 - Sabab</b>

🔍 <b>Qoida:</b> Norasmiy sabab tushuntirish
💡 <b>Misollar:</b>
1. 못 가요. 바쁘거든요 "Bora olmayman. Bandman chunki"
2. 좋아해요. 맛있거든요 "Yoqadi. Mazali chunki"
🎯 <b>Dalil va sabab berish</b>"""

    # Default
    else:
        return f"""🤖 <b>Grammar AI - Professional</b>

🔍 <b>Savolingiz:</b> "{user_input}"

📚 <b>40+ grammar qoidasi mavjud!</b>

💡 <b>Mashhur qoidalar:</b>
• 은/는, 이/가, 을/를 - asosiy belgiler
• 에서, 에게, 와/과, 도, 만 - joy va bog'lovchilar  
• 고, 지만, 려고, 는데 - bog'lovchi shakllari
• 아도/어도, 거든요 - murakkab qoidalar

🎯 <b>Misol:</b> "에서 nima?", "지만 qanday?"

Professional Grammar AI xizmatdasiz! 📖"""

def get_japanese_grammar_explanation(user_input):
    """Yapon grammar tushuntirish AI funksiyasi - Fixed"""
    input_text = user_input.lower()
    
    # Basic particles
    if any(word in input_text for word in ["は", "wa", "mavzu"]):
        return """📚 <b>は (wa) - Mavzu belgisi</b>

🔍 <b>Qoida:</b> は harfi "wa" deb o'qiladi
💡 <b>Misollar:</b>
1. 私は学生です "Men talabaman"
2. 本は面白いです "Kitob qiziqarli"
🎯 <b>Eslab qoling:</b> は = "wa" tovushi"""

    elif any(word in input_text for word in ["が", "ga", "egalik"]):
        return """📚 <b>が (ga) - Egalik belgisi</b>

🔍 <b>Qoida:</b> Gapning egasini aniq ko'rsatadi
💡 <b>Misollar:</b>
1. 猫が可愛いです "Mushuk chiroyli"
2. 誰が来ますか？ "Kim keladi?"
🎯 <b>は dan farqli, aniq egani ko'rsatadi</b>"""

    elif any(word in input_text for word in ["を", "wo", "o", "to'ldiruvchi"]):
        return """📚 <b>を (wo) - To'ldiruvchi belgisi</b>

🔍 <b>Qoida:</b> を harfi "wo" deb o'qiladi
💡 <b>Misollar:</b>
1. りんごを食べます "Olma yeyapman"
2. 本を読みます "Kitob o'qiyapman"
🎯 <b>Eslab qoling:</b> を = "wo" tovushi"""

    # Location particles
    elif any(word in input_text for word in ["に", "ni", "joy", "vaqt"]):
        return """📚 <b>に (ni) - Joy/Vaqt belgisi</b>

🔍 <b>Qoida:</b> Vaqt va joyni ko'rsatadi
💡 <b>Misollar:</b>
1. 学校に行きます "Maktabga boraman"
2. 7時に起きます "7 da turamam"
🎯 <b>Yo'nalish va vaqt uchun</b>"""

    elif any(word in input_text for word in ["で", "de", "vosita"]):
        return """📚 <b>で (de) - Joy/Vosita belgisi</b>

🔍 <b>Qoida:</b> Harakat joyi va vositani ko'rsatadi
💡 <b>Misollar:</b>
1. 図書館で勉強します "Kutubxonada o'qiyman"
2. バスで行きます "Avtobus bilan boraman"
🎯 <b>に dan farqli, harakat joyini ko'rsatadi</b>"""

    # Verb forms
    elif any(word in input_text for word in ["です", "desu", "hisoblanadi"]):
        return """📚 <b>です - "Hisoblanadi"</b>

🔍 <b>Qoida:</b> Rasmiy "hisoblanadi" fe'li
💡 <b>Misollar:</b>
1. 私は学生です "Men talabaman"
2. これは本です "Bu kitob"
🎯 <b>Gapning oxirida keladi</b>"""

    elif any(word in input_text for word in ["ます", "masu", "rasmiy"]):
        return """📚 <b>ます - Rasmiy fe'l</b>

🔍 <b>Qoida:</b> Rasmiy va muloyim so'lash
💡 <b>Misollar:</b>
1. 食べます "Yeyapman"
2. 行きます "Borayapman"
🎯 <b>Hozirgi va kelajak uchun</b>"""

    elif any(word in input_text for word in ["た", "ta", "o'tgan"]):
        return """📚 <b>た - O'tgan zamon</b>

🔍 <b>Qoida:</b> O'tgan zamondagi harakat
💡 <b>Misollar:</b>
1. 食べた "Yedim"
2. 行った "Bordim"
🎯 <b>Oddiy o'tgan zamon</b>"""

    elif any(word in input_text for word in ["ている", "te iru", "davomiy"]):
        return """📚 <b>ている - Hozirgi davomiy</b>

🔍 <b>Qoida:</b> Hozirda davom etayotgan harakat
💡 <b>Misollar:</b>
1. 食べている "Yeyapmaqda"
2. 勉強している "O'qiyapmaqda"
🎯 <b>Hozirgi davomiy harakat</b>"""

    elif any(word in input_text for word in ["でしょう", "deshou", "ehtimol"]):
        return """📚 <b>でしょう - Ehtimol</b>

🔍 <b>Qoida:</b> Taxmin va ehtimollik
💡 <b>Misollar:</b>
1. 雨でしょう "Yomg'ir yog'ar shekilli"
2. 美味しいでしょう "Mazali bo'lar ehtimol"
🎯 <b>Yumshoq taxmin</b>"""

    # Default
    else:
        return f"""🤖 <b>Grammar AI - Professional</b>

🔍 <b>Savolingiz:</b> "{user_input}"

📚 <b>20+ grammar qoidasi mavjud!</b>

💡 <b>Mashhur qoidalar:</b>
• は, が, を - asosiy belgiler
• に, で - joy belgilari
• です, ます - rasmiy shakllar
• た, ている, でしょう - zamon shakllari

🎯 <b>Misol:</b> "は nima?", "ます qanday?"

Professional Grammar AI xizmatdasiz! 📖"""