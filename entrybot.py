import requests, os, csv, time, traceback, datetime
import graphql, utills

pre_id=0
active=True

with requests.Session() as s:
    bot=utills.Bot(s)

    def createComment(text, image=None):
        global pre_id
        if active==True:
            if image==None:
                s.post('https://playentry.org/graphql', headers=bot.headers, json={'query':graphql.createComment, "variables":{"content":text,"target":bot.id,"targetSubject":"discuss","targetType":"individual"}})
            else:
                s.post('https://playentry.org/graphql', headers=bot.headers, json={'query':graphql.createComment, "variables":{"content":text,"image":image,"target":bot.id,"targetSubject":"discuss","targetType":"individual"}})
            pre_id=bot.id

    def createStory(text, image=None):
        if image==None:
            s.post('https://playentry.org/graphql', headers=bot.headers, json={'query':graphql.createStory, "variables":{"content":text}})
        else:
            s.post('https://playentry.org/graphql', headers=bot.headers, json={'query':graphql.createStory, "variables":{"content":text,"image":image}})

    def openAdmin():
        f=open('admin.csv', 'r')
        reader=csv.reader(f)
        f.close()
        output=[]
        for i in reader: output.append(i)
        return output[0]

    def plusAdmin():
        f=open('admin.csv', 'w')
        a=csv.writer(f, delimiter=',')
        a.writerows([adminList])
        f.close()

    while True:
        try:
            time.sleep(0.1)
            bot.setting()
            # if True: # 테스트용
            if pre_id!=bot.id:
                if bot.text[:2] in ['ㅌ ', 't ']:
                    commend=bot.text[2:]
                    # commend='' # 테스트용
                    # 일반 명령어
                    try: createComment(utills.commendList[commend])

                    except:
                        # 추가 동작이 필요한 명령어
                        if  commend in ['폭발', '폭8', '자폭']:
                            createComment('폭8!!!!! 퍼퍼퍼버어어버ㅓㅍ어ㅓ어', '61de946f1e65f8fcf9015350')

                        elif commend[:3]=='유찾 ':
                            rpl=''
                            myPage=bot.userSearchNick(commend[3:])
                            if myPage!=None:
                                rpl=f'playentry.org/profile/{myPage} (닉네임)'
                            myPage=bot.userSearchId(commend[3:])
                            if rpl!='' and myPage!=None:
                                if rpl[22:46]==myPage:
                                    rpl=f'playentry.org/profile/{myPage} (닉네임, 아이디)'
                                else:
                                    rpl=f'{rpl}, playentry.org/profile/{myPage} (아이디)'
                            elif myPage!=None:
                                rpl=f'playentry.org/profile/{myPage} (아이디)'
                            if rpl=='':
                                rpl=f'{commend[3:]} 닉네임/아이디를 가진 유저를 찾을 수 없어요.'
                            else:
                                rpl=f'{commend[3:]}님의 마이페이지 주소는 {rpl} 이에요!'
                            rplPlus=''
                            myPage=bot.userSearchNick(commend[3:]+'_')
                            if myPage!=None:
                                rplPlus=f'playentry.org/profile/{myPage} ({commend[3:]}_)'
                            myPage=bot.userSearchNick(commend[3:]+'ㅤ')
                            if myPage!=None:
                                if rplPlus=='':
                                    rplPlus=f'playentry.org/profile/{myPage} ({commend[3:]}ㅤ)'
                                else:
                                    rplPlus=f'{rplPlus}, playentry.org/profile/{myPage} ({commend[3:]}ㅤ)'
                            myPage=bot.userSearchNick(commend[3:]+'_ㅤ')
                            if myPage!=None:
                                if rplPlus=='':
                                    rplPlus=f'playentry.org/profile/{myPage} ({commend[3:]}_ㅤ)'
                                else:
                                    rplPlus=f'{rplPlus}, playentry.org/profile/{myPage} ({commend[3:]}_ㅤ)'
                            myPage=bot.userSearchNick(commend[3:]+'ㅤㅤ')
                            if myPage!=None:
                                if rplPlus=='':
                                    rplPlus=f'playentry.org/profile/{myPage} ({commend[3:]}ㅤㅤ)'
                                else:
                                    rplPlus=f'{rplPlus}, playentry.org/profile/{myPage} ({commend[3:]}ㅤㅤ)'
                            try:
                                myPage=bot.userSearchId(utills.user[commend[3:]])
                                if myPage!=None:
                                    if rplPlus=='':
                                        rplPlus=f'playentry.org/profile/{myPage} ({utills.user[commend[3:]]})'
                                    else:
                                        rplPlus=f'{rplPlus}, playentry.org/profile/{myPage} ({utills.user[commend[3:]]})'
                            except: pass
                            if rplPlus!='':
                                rpl=f'{rpl} 혹시 이 유저를 찾으시려던 건가요? {rplPlus}'
                            if commend[3:] in ['레몬봇', 'lemonbpt', 'Lemon봇', 'lemonbot']:
                                rpl=f'{rpl} .....그런데 레몬봇을 왜 찾으시나요? 여기 티엔봇이 있답니다!'
                            createComment(rpl)

                        elif commend=='프사':
                            profileImage=bot.profileImage()
                            createComment(f'{bot.authorNick}님의 프로필 사진이에요!', profileImage)

                        elif commend[:3]=='프사 ':
                            myPage=bot.userSearchNick(commend[3:])
                            if myPage==None:
                                createComment(f'{commend[3:]} 닉네임을 가진 유저를 찾을 수 없어요.')
                            else:
                                profileImage=bot.profImgNick(myPage)
                                createComment(f'{commend[3:]}님의 프로필 사진이에요!', profileImage)

                        elif commend=='배사':
                            bgImage=bot.bgImage(bot.authorId)
                            createComment(f'{bot.authorNick}님의 배경 사진이에요!', bgImage)

                        elif commend[:3]=='배사 ':
                            myPage=bot.userSearchNick(commend[3:])
                            if myPage==None:
                                createComment(f'{commend[3:]} 닉네임을 가진 유저를 찾을 수 없어요.')
                            else:
                                bgImage=bot.bgImage(myPage)
                                createComment(f'{commend[3:]}님의 배경 사진이에요!', bgImage)

                        elif commend=='정보':
                            projectCnt, like, comment, view, status, qna, tip, free, popular, staff, mostLike, mostComment, mostView=bot.info(bot.authorId)
                            if status=="USE":
                                status=''
                            elif status=="WARN":
                                status='현재 1차 또는 2차정지 상태입니다.'
                            else:
                                status='영구정지 상태입니다.'
                            if projectCnt==0:
                                createComment(f'{bot.authorNick}님의 작품이 없어요. playentry.org/ws/new 에서 새 작품을 만들어 보세요! 커뮤니티 글 {qna+tip+free}개 중 묻고 답하기 {qna}개, 노하우&팁 {tip}개, 엔트리 이야기 {free}개입니다. {status}')
                            else:
                                createComment(f'{bot.authorNick}님의 작품 {projectCnt}개의 총 좋아요 수는 {like}개, 댓글 수는 {comment}개, 조회수는 {view}회 입니다. 좋아요 가장 많은 작품 playentry.org/project/{mostLike}, 댓글 가장 많은 작품 playentry.org/project/{mostComment}, 조회수 가장 많은 작품 playentry.org/project/{mostView}. 인작 {popular}개, 스선 {staff}개. 커뮤니티 글 {qna+tip+free}개 중 묻고 답하기 {qna}개, 노하우&팁 {tip}개, 엔트리 이야기 {free}개입니다. {status}')

                        elif commend[:3]=='정보 ':
                            myPage=bot.userSearchNick(commend[3:])
                            projectCnt, like, comment, view, status, qna, tip, free, popular, staff, mostLike, mostComment, mostView=bot.info(myPage)
                            if status=="USE":
                                status=''
                            elif status=="WARN":
                                status='현재 1차 또는 2차정지 상태입니다.'
                            else:
                                status='영구정지 상태입니다.'
                            if projectCnt==0:
                                createComment(f'{commend[3:]}님의 작품이 없어요. playentry.org/ws/new 에서 새 작품을 만들어 보세요! 커뮤니티 글 {qna+tip+free}개 중 묻고 답하기 {qna}개, 노하우&팁 {tip}개, 엔트리 이야기 {free}개입니다. {status}')
                            else:
                                createComment(f'{commend[3:]}님의 작품 {projectCnt}개의 총 좋아요 수는 {like}개, 댓글 수는 {comment}개, 조회수는 {view}회 입니다. 좋아요 가장 많은 작품 playentry.org/project/{mostLike}, 댓글 가장 많은 작품 playentry.org/project/{mostComment}, 조회수 가장 많은 작품 playentry.org/project/{mostView}. 인작 {popular}개, 스선 {staff}개. 커뮤니티 글 {qna+tip+free}개 중 묻고 답하기 {qna}개, 노하우&팁 {tip}개, 엔트리 이야기 {free}개입니다. {status}')

                        elif commend=='랜덤작':
                            project, name, nick, des=bot.ranProject()
                            createComment(f'{nick}님의 {name} 작품은 어때요? playentry.org/project/{project} {des}')

                        elif commend[:4]=='랜덤작 ':
                            if commend[4:] in ['게임', '생활과 도구', '스토리텔링', '예술', '지식 공유', '기타']:
                                project, name, nick, des=bot.ranProject(commend[4:])
                                createComment(f'{nick}님의 {name} 작품은 어때요? playentry.org/project/{project} {des}')
                            else:
                                createComment('게임, 생활과 도구, 스토리텔링, 예술, 지식 공유, 기타 중 하나의 카테고리를 선택해주세요!')

                        elif commend[:4]=='글찾기 ':
                            createComment('제작중...')

                        elif commend[:5]=='노팁찾기 ':
                            createComment('제작중...')

                        elif commend in ['스선분석', '스선 분석']:
                            createComment('제작중...')

                        # 관리 명령어
                        elif commend[:7]=='관리자 추가 ':
                            adminList=openAdmin()
                            if bot.authorId in adminList:
                                if commend[7:] in adminList:
                                    createComment('이미 관리자 목록에 추가되어 있어요.')
                                else:
                                    adminList.append(commend[7:])
                                    plusAdmin()
                                    createComment('관리자 추가가 완료되었습니다.')
                            else: createComment('관리자만 사용할 수 있는 명령어입니다.')

                        elif commend=='시작':
                            adminList=openAdmin()
                            if bot.authorId in adminList:
                                if active==True:
                                    createComment('이미 작동하고 있습니다.')
                                else:
                                    active=True
                                    createComment('티엔봇 작동을 시작합니다.')
                                    createStory('티엔봇 작동을 시작합니다.')
                            else: createComment('관리자만 사용할 수 있는 명령어입니다.')

                        elif commend=='중지':
                            adminList=openAdmin()[0]
                            if bot.authorId in adminList:
                                if active==True:
                                    createComment('티엔봇 작동을 중지합니다.')
                                    active=False
                                    createStory('티엔봇 작동을 중지합니다.')
                            else: createComment('관리자만 사용할 수 있는 명령어입니다.')

                        # 명령어 끝
                        else: createComment('아직 지원하지 않는 명령어에요.')
                elif bot.text=='ㅌ': createComment('부르셨나요?')

        # 에러 출력
        except:
            if traceback.format_exc()[-18:-1]=='KeyboardInterrupt':
                print('티엔봇 종료')
                break
            print('\n========== ERROR ==========')
            print(f'\nTime: {datetime.datetime.now()}')
            print(f'Text URL: playentry.org/community/entrystory/{bot.id}')
            print(f'Text: {bot.text}\n')
            print(traceback.format_exc())
            print('===========================')
