# 여행 블로그
Django를 활용한 여행 블로그 웹 프로젝트입니다.

## 1. 목표와 구현 기능
### 1.1 목표
### 1.2 기능

## 2. 개발 환경 및 배포 URL
### 2.1 개발 환경
### 2.2 URL 구조(모놀리식)
- Main App URLs

| URL Pattern | View Name | Description |
|-------------|-----------|-------------|
| `admin/` | admin.site.urls | 관리자 페이지 |
| `''` | include('posts.urls') | posts URL 포함 |
| `accounts/` | include('accounts.urls') | accounts URL 포함 |
| `interactions/` | include('interactions.urls') | interactions URL 포함 |

- Accounts App URLs

| URL Pattern | View Name | Description |
|-------------|-----------|-------------|
| `signup/` | signup | 유저 회원가입 |
| `login/` | login | 유저 로그인 |
| `logout/` | logout | 유저 로그아웃 |
| `profile/` | profile | 유저 프로필 열람 |
| `profile/edit/` | edit_profile | 유저 프로필 수정 |
| `password/change/` | change_password | 유저 비밀번호 수정 |

- Posts App URLs

| URL Pattern | View Name | Description |
|-------------|-----------|-------------|
| `''` | home | Home page |
| `post/new/` | post_new | 새 게시글 생성(로그인 필요) |
| `post/<int:pk>/` | post_detail | 특정 게시글 열람 |
| `post/<int:pk>/edit/` | post_edit | 게시글 수정(로그인 필요, 본인 글만 가능) |
| `post/<int:pk>/delete/` | post_delete | 게시글 삭제(로그인 필요, 본인 글만 가능) |
| `posts/` | post_list | 모든 게시글의 리스트 |
| `category/<slug:category_slug>/` | category_posts | 카테고리별 게시글 리스트 |
| `tag/<slug:tag_slug>/` | tag_posts | 태그별 게시글 리스트 |
| `search/` | search_posts | 게시글 검색 |

- Interactions App URLs

| URL Pattern | View Name | Description |
|-------------|-----------|-------------|
| `post/<int:pk>/comment/` | add_comment | 게시글 댓글(로그인 필요) |
| `comment/<int:pk>/reply/` | add_reply | 게시글 댓글의 대댓글(로그인 필요) |
| `comment/<int:pk>/edit/` | edit_comment | 댓글 수정(로그인 필요, 본인 글만 가능) |
| `comment/<int:pk>/delete/` | delete_comment | 댓글 삭제(로그인 필요, 본인 글만 가능) |
| `post/<int:pk>/like/` | like_post | 게시글 좋아요 기능 |
| `post/<int:pk>/bookmark/` | bookmark_post | 북마크 기능(로그인 필요) |
| `notifications/` | notifications | 유저 알림(로그인 필요) |

## 3. 프로젝트 구조와 개발 일정
### 3.1 프로젝트 구조
### 3.2 개발 일정(WBS)
```mermaid
gantt
    title Django 블로그 프로젝트 WBS
    dateFormat  YYYY-MM-DD
    axisFormat %m-%d
    
    section 프로젝트 준비
    프로젝트 기획       :2023-08-26, 1d
    WBS 작성            :2023-08-26, 1d
    기획서 작성         :2023-08-27, 1d
    와이어프레임 작성   :2023-08-27, 1d
    
    section 데이터베이스 설계
    ERD 작성            :2023-08-27, 1d
    모델 설계           :2023-08-28, 1d
    
    section 기본 구조 설계
    URL 설계            :2023-08-28, 1d
    프로젝트 셋업       :2023-08-28, 4h
    기본 템플릿 구성    :2023-08-28, 4h
    
    section 핵심 기능 구현
    메인페이지          :2023-08-29, 4h
    회원가입 기능       :2023-08-29, 4h
    로그인/로그아웃 기능:2023-08-29, 4h
    게시글 CRUD 기능    :2023-08-29, 1d
    
    section 부가 기능 구현
    댓글 기능           :2023-08-30, 6h
    태그 및 카테고리 기능:2023-08-30, 6h
    좋아요 및 북마크 기능:2023-08-30, 6h
    알림 시스템         :2023-08-30, 6h
    
    section 마무리
    테스트 및 디버깅    :2023-08-30, 4h
    문서화              :2023-08-30, 2h
```
## 4. 와이어프레임

## 5. 데이터베이스 모델링(ERD)
```mermaid
erDiagram
    User ||--o{ Post : writes
    User ||--o{ Comment : makes
    User ||--o{ Like : gives
    User ||--o{ Bookmark : saves
    User ||--o{ Notification : receives
    Post ||--o{ Comment : has
    Post ||--o{ Like : receives
    Post ||--o{ Bookmark : has
    Post }o--|| Category : belongs_to
    Post }o--o{ Tag : has

    User {
        int id PK
        string username
        string email
        string nickname
        boolean is_staff
        boolean is_active
        boolean is_superuser
        datetime date_joined
    }

    Post {
        int id PK
        string title
        text content
        datetime created_at
        datetime updated_at
        int author FK
        int category FK
        int views
    }

    Category {
        int id PK
        string name
        string slug
    }

    Comment {
        int id PK
        text content
        datetime created_at
        datetime updated_at
        int author FK
        int post FK
        int parent FK
    }

    Like {
        int id PK
        int user FK
        int post FK
        datetime created_at
    }

    Bookmark {
        int id PK
        int user FK
        int post FK
        datetime created_at
    }

    Notification {
        int id PK
        string notification_type
        int recipient FK
        int actor FK
        string verb
        int target FK
        datetime created_at
        boolean is_read
    }

    Tag {
        int id PK
        string name
        string slug
    }
```
## 6. 메인 기능
## 7. 에러와 에러 해결
## 8. 회고
