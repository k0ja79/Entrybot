login='''
    mutation (
        $username: String!, 
        $password: String!, 
        $rememberme: Boolean, 
        $captchaValue: String, 
        $captchaKey: String,
        $captchaType: String
    ) {
        signinByUsername (
            username: $username, 
            password: $password, 
            rememberme: $rememberme, 
            captchaValue: $captchaValue, 
            captchaKey: $captchaKey,
            captchaType: $captchaType
        ) {
            
    id
    username
    nickname
    role
    isEmailAuth
    isSnsAuth
    isPhoneAuth
    studentTerm
    alarmDisabled
    status {
        userStatus
    }
    profileImage {
        
    id
    name
    label {
        
    ko
    en
    ja
    vn

    }
    filename
    imageType
    dimension {
        
    width
    height

    }
    trimmed {
        filename
        width
        height
    }

    }
    banned {
        username
        nickname
        reason
        bannedCount
        bannedType
        projectId
        startDate
        userReflect {
            status
            endDate
        }
    }
    isProfileBlocked

        }
    }'''
createStory='''
    mutation CREATE_ENTRYSTORY(
        
    $content: String
    $text: String
    $image: String
    $sticker: ID
    $stickerItem: ID
    $cursor: String

    ) {
        createEntryStory(
            
    content: $content
    text: $text
    image: $image
    sticker: $sticker
    stickerItem: $stickerItem
    cursor: $cursor

        ) {
            warning
            discuss{
                
    id
    title
    content
    seContent
    created
    commentsLength
    likesLength
    visit
    category
    prefix
    groupNotice
    user {
        
    id
    nickname
    username
    profileImage {
        
    id
    name
    label {
        
    ko
    en
    ja
    vn

    }
    filename
    imageType
    dimension {
        
    width
    height

    }
    trimmed {
        filename
        width
        height
    }

    }
    status {
        following
        follower
    }
    description
    role

    }
    images {
        filename
        imageUrl
    }
    sticker {
        
    id
    name
    label {
        
    ko
    en
    ja
    vn

    }
    filename
    imageType
    dimension {
        
    width
    height

    }
    trimmed {
        filename
        width
        height
    }

    }
    progress
    thumbnail
    reply
    bestComment {
        
    id
    user {
        
    id
    nickname
    username
    profileImage {
        
    id
    name
    label {
        
    ko
    en
    ja
    vn

    }
    filename
    imageType
    dimension {
        
    width
    height

    }
    trimmed {
        filename
        width
        height
    }

    }
    status {
        following
        follower
    }
    description
    role

    }
    content
    created
    removed
    blamed
    commentsLength
    likesLength
    isLike
    hide
    image {
        
    id
    name
    label {
        
    ko
    en
    ja
    vn

    }
    filename
    imageType
    dimension {
        
    width
    height

    }
    trimmed {
        filename
        width
        height
    }

    }
    sticker {
        
    id
    name
    label {
        
    ko
    en
    ja
    vn

    }
    filename
    imageType
    dimension {
        
    width
    height

    }
    trimmed {
        filename
        width
        height
    }

    }

    }
    blamed

            }
        }
    }'''
createComment='''
    mutation CREATE_COMMENT(
        
    $content: String
    $image: String
    $sticker: ID
    $stickerItem: ID
    $target: String
    $targetSubject: String
    $targetType: String
    $groupId: ID

    ) {
        createComment(
            
    content: $content
    image: $image
    sticker: $sticker
    stickerItem: $stickerItem
    target: $target
    targetSubject: $targetSubject
    targetType: $targetType
    groupId: $groupId

        ) {
            warning
            comment {
                
    id
    user {
        
    id
    nickname
    username
    profileImage {
        
    id
    name
    label {
        
    ko
    en
    ja
    vn

    }
    filename
    imageType
    dimension {
        
    width
    height

    }
    trimmed {
        filename
        width
        height
    }

    }
    status {
        following
        follower
    }
    description
    role

    }
    content
    created
    removed
    blamed
    commentsLength
    likesLength
    isLike
    hide
    image {
        
    id
    name
    label {
        
    ko
    en
    ja
    vn

    }
    filename
    imageType
    dimension {
        
    width
    height

    }
    trimmed {
        filename
        width
        height
    }

    }
    sticker {
        
    id
    name
    label {
        
    ko
    en
    ja
    vn

    }
    filename
    imageType
    dimension {
        
    width
    height

    }
    trimmed {
        filename
        width
        height
    }

    }

            }
        }
    }'''
loadStory='''
    query SELECT_ENTRYSTORY(
    $pageParam: PageParam
    $query: String
    $user: String
    $category: String
    $term: String
    $prefix: String
    $progress: String
    $discussType: String
    $searchType: String
    $searchAfter: JSON
){
        discussList(
    pageParam: $pageParam
    query: $query
    user: $user
    category: $category
    term: $term
    prefix: $prefix
    progress: $progress
    discussType: $discussType
    searchType: $searchType
    searchAfter: $searchAfter
) {
            total
            list {
                
	id
    content
    created
    commentsLength
    likesLength
    user {
        
    id
    nickname
    username
    profileImage {
        
    id
    name
    label {
        
    ko
    en
    ja
    vn

    }
    filename
    imageType
    dimension {
        
    width
    height

    }
    trimmed {
        filename
        width
        height
    }

    }
    status {
        following
        follower
    }
    description
    role

    }
    image {
        
    id
    name
    label {
        
    ko
    en
    ja
    vn

    }
    filename
    imageType
    dimension {
        
    width
    height

    }
    trimmed {
        filename
        width
        height
    }

    }
    sticker {
        
    id
    name
    label {
        
    ko
    en
    ja
    vn

    }
    filename
    imageType
    dimension {
        
    width
    height

    }
    trimmed {
        filename
        width
        height
    }

    }
    isLike

            }
            searchAfter
        }
    }'''
loadMypage='''
    query FIND_USERSTATUS_BY_USERNAME($id: String) {
        userstatus(id: $id) {
            id
            nickname
            username
            description
            shortUrl
            profileImage {
                
    id
    name
    label {
        
    ko
    en
    ja
    vn

    }
    filename
    imageType
    dimension {
        
    width
    height

    }
    trimmed {
        filename
        width
        height
    }

            }
            coverImage {
                
    id
    name
    label {
        
    ko
    en
    ja
    vn

    }
    filename
    imageType
    dimension {
        
    width
    height

    }
    trimmed {
        filename
        width
        height
    }

            }
            role
            studentTerm
            status {
                project
                projectAll
                study
                studyAll
                community {
                    qna
                    tips
                    free
                }
                following
                follower
                bookmark {
                    project
                    study
                }
                userStatus
            }
        }
    }'''
loadProject='''
    query SELECT_USER_PROJECTS(
        
    $user: String!
    $query: String
    $categoryCode: String
    $groupId: ID
    $pageParam: PageParam
    $isOpen: Boolean
    $except: [ID]
    $searchAfter: JSON
    $searchType: String
    $term: String

    ) {
        userProjectList(
            
    user: $user
    query: $query
    categoryCode: $categoryCode
    groupId: $groupId
    pageParam: $pageParam
    isOpen: $isOpen
    except: $except
    searchAfter: $searchAfter
    searchType: $searchType
    term: $term

    ) {
            total
            list {
                
    id
    name
    user {
        id
        username
        nickname
        profileImage {
            id
            filename
            imageType
        }
    }
    thumb
    isopen
    isPracticalCourse
    category
    categoryCode
    created
    updated
    special
    isForLecture
    isForStudy
    isForSubmit
    hashId
    complexity
    staffPicked
    ranked
    visit
    likeCnt
    comment

            }
            searchAfter
        }
    }'''
userSearchNick='''query ($nickname: String) { user(nickname: $nickname) { id } }'''
userSearchId='''query ($username: String) { user(username: $username) { id } }'''
project='''
    query SELECT_PROJECTS(
        
    $query: String 
    $categoryCode: String
    $staffPicked: Boolean
    $ranked: Boolean
    $parent: String
    $origin: String
    $discovery: String
    $pageParam: PageParam
    $term: String
    $queryTitleOnly:Boolean
    $isChallenge:Boolean
    $searchAfter: JSON
    $searchType: String
    $cacheKey: String

    ) {
        projectList(
            
    query: $query
    categoryCode: $categoryCode
    staffPicked: $staffPicked
    ranked: $ranked
    parent: $parent
    origin: $origin
    discovery: $discovery
    pageParam: $pageParam
    term: $term
    queryTitleOnly: $queryTitleOnly
    isChallenge: $isChallenge
    searchAfter: $searchAfter
    searchType: $searchType
    cacheKey: $cacheKey

        ) {
            total
            list {
                
    id
    name
    user {
        id
        username
        nickname
        profileImage {
            id
            filename
            imageType
        }
    }
    thumb
    isopen
    isPracticalCourse
    category
    categoryCode
    created
    updated
    special
    isForLecture
    isForStudy
    isForSubmit
    hashId
    complexity
    staffPicked
    ranked
    visit
    likeCnt
    comment

            }
            last
            searchAfter
        }
    }'''
projectDetail='''
    query SELECT_PROJECT_LITE($id: ID! $groupId: ID) {
        project(id: $id, groupId: $groupId) {
            
    id
    name
    user {
        
    id
    nickname
    username
    profileImage {
        
    id
    name
    label {
        
    ko
    en
    ja
    vn

    }
    filename
    imageType
    dimension {
        
    width
    height

    }
    trimmed {
        filename
        width
        height
    }

    }
    status {
        following
        follower
    }
    description
    role

    }
    thumb
    isopen
    blamed
    isPracticalCourse
    category
    categoryCode
    created
    updated
    special
    isForLecture
    isForStudy
    isForSubmit
    hashId
    complexity
    staffPicked
    ranked
    visit
    likeCnt
    comment
    favorite
    shortenUrl
    parent {
        id
        name
        user {
            id
            username
            nickname
        }
    }
    description
    description2
    description3
    hasRealTimeVariable
    childCnt
    commentGroup {
        group
        count
    }
    likeCntGroup {
        group
        count
    }
    visitGroup {
        group
        count
    }
    recentGroup {
        group
        count
    }

        }
     }'''
