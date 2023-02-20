import requests, datetime, re, random, os, json
from bs4 import BeautifulSoup as bs
import graphql

commendList={
    '바보': '제 부족한 점을 알려주시면 개선하도록 노력할게요ㅠㅠ', '싫어': '제 부족한 점을 알려주시면 개선하도록 노력할게요ㅠㅠ',
    '샍': '와! 샌즈 아시네요!', '샌즈': '와! 샌즈 아시네요!', '샌주': '와! 샌즈 아시네요!',
    '개발자': '저의 개발자는 TN_티엔님( playentry.org/profile/5961bba619181b9033e53f8e )이에요!', '제작자': '저의 개발자는 TN_티엔님( playentry.org/profile/5961bba619181b9033e53f8e )이에요!',
    '사랑해': '감사합니다!', '고마워': '감사합니다!', '잘했어': '감사합니다!',
    '명령어': 'naver.me/5UGa0Vxs 이 작품을 참고해주세요!', '도움말': 'naver.me/5UGa0Vxs 이 작품을 참고해주세요!',
    '티엔': '티엔님은 제 귀여운 개발자님이세요!',
    '심심해': '엔트리에 있는 재미있는 작품을 플래이해보는건 어떨까요?',
    '슬랭': 'slang.place/start/intro 슬랭 쓸랭?',
    '엔트리위키': '엔트리에 관한 문서를 읽어보세요! playentry.miraheze.org (기엽고 깜찍한 도뜨의 엔트리위키), docs.playentry.org/user(공식 엔트리위키)',
    '공백': "'​'(U+200b), ' '(U+0020, 반각 공백), '　'(U+3000, 전각 공백), 'ᅟ'(U+115F, 한글 초성 채움 문자), 'ᅠ'(U+1160, 한글 중성 채움 문자), 'ㅤ'(U+3164, 한글 채움 문자), 'ﾠ'(U+FFA0, 반각 한글 채움 문자), '⠀' (U+2800, 점자 패턴 공백)", '공백문자': "'​'(U+200b), ' '(U+0020, 반각 공백), '　'(U+3000, 전각 공백), 'ᅟ'(U+115F, 한글 초성 채움 문자), 'ᅠ'(U+1160, 한글 중성 채움 문자), 'ㅤ'(U+3164, 한글 채움 문자), 'ﾠ'(U+FFA0, 반각 한글 채움 문자), '⠀' (U+2800, 점자 패턴 공백)",
    '코드': '코드를 공개하면 악용할 가능성이 있어서 공개는 힘들 것 같아요...', '코드 공개': '코드를 공개하면 악용할 가능성이 있어서 공개는 힘들 것 같아요...',
    '뭐해': '뭐하긴요! 당신 생각하고 있었어요!', '뭐해?': '뭐하긴요! 당신 생각하고 있었어요!',
    '귀여워': '제가 좀 귀엽죠? 뀨 :3',
    '스선 언제돼': '열심히 노력하다 보면 언젠간 될거에요!',
    '티엔 귀여워': '물론이죠!',
    '천재': '님이 더 재수없거든요? 흥!',
    '신기해': '훗! 제가 좀 신기하죠?',
    '안신기해': '괜찮아요. 저는 여러분의 편의를 위해 만들어졌으니까요.',
    '?': '??????????',
    '최고': '당신도 최고!',
    '날짜': f'오늘 날짜는 {datetime.date.today()} 이에요!', '연도': f'오늘은 {datetime.date.today().year}년 이에요!', '몇월': f'오늘은 {datetime.date.today().month}월 이에요!', '몇일': f'오늘은 {datetime.date.today().day}일 이에요!', '시각': f'지금은 {datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second} 이에요!', '현재시각': f'지금은 {datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second} 이에요!', '몇시': f'지금은 {datetime.datetime.now().hour}시 에요!', '몇분': f'지금은 {datetime.datetime.now().minute}분 이에요!', '몇초': f'지금은 {datetime.datetime.now().second}.{datetime.datetime.now().microsecond}초 에요!',
    '그림 못그려': '하지만 전 코딩을 잘하니까 괜찮아요.',
    '댓글 달아줘': '달아줄까말까',
    '자동이야?': '네, 자동이에요.',
    '어딨어?': '당신의 마음속에요~',
    '수동이야?': '아니요, 자동이에요.',
    '나 귀여워?': '물론 당신도 귀엽지만 티엔이 제일 귀여워요.',
    '누구야?': '저는 티엔봇일까요?',
    '못생김': '당신보단 낫지 않을까요?',
    '잘가': '다음에 또 봐요!',
    '응애': '응애 나 아기 티엔',
    '뀨': '뀨? :3',
    'ㅈㅅㄱ': '안녕히가세요!',
    '세부정보': "이전의 'ㅌ 세부정보' 기능은 'ㅌ 정보' 명령어로 통합되었어요!",
}
categoryList={'게임':'game', '생활과 도구':'living', '스토리텔링':'storytelling', '예술':'arts', '지식 공유':'knowledge', '기타':'etc'}
user={'티엔': 'tnghks1'}
story=0

class Bot:
    global story
    def __init__(self, s):
        loginPage = s.get('https://playentry.org/signin')
        soup = bs(loginPage.text, 'html.parser')
        csrf = soup.find('meta', {'name': 'csrf-token'})
        login_headers={'CSRF-Token': csrf['content'], "Content-Type": "application/json"}
        s.post('https://playentry.org/graphql', headers=login_headers, json={'query':graphql.login, 'variables':{"username":"tnghks8","password":os.environ['mypw']}})
        xtoken=bs(s.get('https://playentry.org/').text, 'html.parser')
        xtoken=xtoken.find('script', {'id':'__NEXT_DATA__'}).text
        xtoken=json.loads(xtoken)['props']['initialState']['common']['user']['xToken']
        self.headers={'X-Token': xtoken, 'x-client-type': 'Client', 'CSRF-Token': csrf['content'], "Content-Type": "application/json"}
        self.session=s

    def setting(self):
        req=self.session.post('https://playentry.org/graphql', headers=self.headers, json={'query':graphql.loadStory, "variables":{"category":"free","searchType":"scroll","term":"all","discussType":"entrystory","pageParam":{"display":1,"sort":"created"}}})
        # story=req.text # 엔이 글 요청 응답
        story=json.loads(req.text)
        self.text=story['data']['discussList']['list'][0]['content']
        # self.text=story[92:story.index('","created":')] # 최신글
        try:
            self.text=self.text[:self.text.index('&::')]
        except: pass
        self.id=story['data']['discussList']['list'][0]['id']
        self.authorId=story['data']['discussList']['list'][0]['user']['id']
        self.authorNick=story['data']['discussList']['list'][0]['user']['nickname']
        # self.id=story[55:story.index('","content":"')] # 글 id
        # self.authorId=story[story.index('"user":{"id":"')+14:story.index('"user":{"id":"')+14+24] # 작성자 id
        # self.authorNick=story[story.index('","nickname":"')+14:story.index('","username":"')] # 작성자 닉네임

    def bgImage(self, id):
        req=self.session.post('https://playentry.org/graphql', headers=self.headers, json={'query':graphql.loadMypage, "variables":{"id":id}})
        myPage=req.text
        bgImage=myPage[myPage.index('"coverImage":{"id":"')+20:myPage.index('"coverImage":{"id":"')+20+24]
        return bgImage

    def profileImage(self, id):
        req=self.session.post('https://playentry.org/graphql', headers=self.headers, json={'query':graphql.loadMypage, "variables":{"id":id}})
        myPage=req.text
        profileImage=myPage[myPage.index('"profileImage":{"id":"')+22:myPage.index('"profileImage":{"id":"')+22+24]
        return profileImage

    def userSearchId(self, id):
        req=self.session.post('https://playentry.org/graphql', headers=self.headers, json={'query':graphql.userSearchId, "variables":{"username":id}})
        userSearch=req.text
        try:
            myPage=userSearch[userSearch.index('"id":"')+6:userSearch.index('"id":"')+6+24]
            return myPage
        except: return None

    def userSearchNick(self, nick):
        req=self.session.post('https://playentry.org/graphql', headers=self.headers, json={'query':graphql.userSearchNick, "variables":{"nickname":nick}})
        userSearch=req.text
        try:
            myPage=userSearch[userSearch.index('"id":"')+6:userSearch.index('"id":"')+6+24]
            return myPage
        except: return None

    def info(self, id):
        like, comment, view=0, 0, 0 # 총합
        mostLike, mostComment, mostView=[0, 0], [0, 0], [0, 0] # [좋아요 수, id]
        req=self.session.post('https://playentry.org/graphql', headers=self.headers, json={'query':graphql.loadMypage, "variables":{"id":id}})
        myPage=json.loads(req.text)
        projectCnt=myPage['data']['userstatus']['status']['project']
        status=myPage['data']['userstatus']['status']['userStatus']
        qna=myPage['data']['userstatus']['status']['community']['qna']
        tip=myPage['data']['userstatus']['status']['community']['tips']
        free=myPage['data']['userstatus']['status']['community']['free']
        
        req=self.session.post('https://playentry.org/graphql', headers=self.headers, json={'query':graphql.loadProject, "variables":{"searchType":"scroll","user":id,"term":"all","pageParam":{"display":projectCnt,"sort":"created"}}})
        myPage=json.loads(req.text)
        project=myPage['data']['userProjectList']['list']
        popular, staff=0, 0
        likeCnt, commentCnt, viewCnt, projectId=[], [], [], []
        for i in project:
            if i['ranked']!=None:
                popular+=1
            if i['staffPicked']!=None:
                staff+=1
            likeCnt.append(i['likeCnt'])
            commentCnt.append(i['comment'])
            viewCnt.append(i['visit'])
            projectId.append(i['id'])

        num=0
        for i in likeCnt:
            like+=i
            if i>=mostLike[0]: mostLike=[i, projectId[num]]
            num+=1
        num=0
        for i in commentCnt:
            comment+=i
            if i>=mostComment[0]: mostComment=[i, projectId[num]]
            num+=1
        num=0
        for i in viewCnt:
            view+=i
            if i>=mostView[0]: mostView=[i, projectId[num]]
            num+=1
        return projectCnt, like, comment, view, status, qna, tip, free, popular, staff, mostLike[1], mostComment[1], mostView[1]
    
    def ranProject(self, category=None):
        if category==None:
            req=self.session.post('https://playentry.org/graphql', headers=self.headers, json={'query':graphql.project, "variables":{"query":"","term":"week","listName":"projectList","searchType":"scroll","pageParam":{"sort":"likeCnt","display":100}}})
        else:
            req=self.session.post('https://playentry.org/graphql', headers=self.headers, json={'query':graphql.project, "variables":{"query":"","categoryCode":categoryList[category],"term":"week","listName":"projectList","searchType":"scroll","pageParam":{"sort":"likeCnt","display":100}}})
        projShare=req.text
        project=re.findall(r'[\[|},]{"id":".{24}?"', projShare)
        name=re.findall(r'","name":".+?",', projShare)
        nick=re.findall(r'","nickname":".+?",', projShare)
        nick=re.findall(r'","nickname":".+?",', projShare)
        num=0
        for i in project:
            project[num]=i[8:-1]
            num+=1
        num=0
        for i in name:
            name[num]=i[10:-2]
            num+=1
        num=0
        for i in nick:
            nick[num]=i[14:-2]
            num+=1
        num=random.randint(0, len(project)-1)
        req=self.session.post('https://playentry.org/graphql', headers=self.headers, json={'query':graphql.projectDetail, "variables":{"id":project[num]}})
        projShare=req.text
        des=projShare[projShare.index('"parent"'):]
        des=des[des.index('"description":')+14:des.index(',"description2"')]
        if des=='null':
            des=''
        else:
            des=des[1:-1]
            des=re.sub(r'\\n', ' ', des)
            des=re.sub(r'\\', ' ', des)
            des=re.sub('  ', ' ', des)
            if len(des)>=150:
                des=des[:151]+'...'
        return project[num], name[num], nick[num], des
