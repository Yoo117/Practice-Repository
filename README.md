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
| `admin/` | admin.site.urls | Django admin interface |
| `''` | include('posts.urls') | Include all posts URLs |
| `accounts/` | include('accounts.urls') | Include all accounts URLs |
| `interactions/` | include('interactions.urls') | Include all interactions URLs |

- Accounts App URLs

| URL Pattern | View Name | Description |
|-------------|-----------|-------------|
| `signup/` | signup | User registration |
| `login/` | login | User login |
| `logout/` | logout | User logout |
| `profile/` | profile | User profile view |
| `profile/edit/` | edit_profile | Edit user profile |
| `password/change/` | change_password | Change user password |

- Posts App URLs

| URL Pattern | View Name | Description |
|-------------|-----------|-------------|
| `''` | home | Home page |
| `post/new/` | post_new | Create new post |
| `post/<int:pk>/` | post_detail | View post details |
| `post/<int:pk>/edit/` | post_edit | Edit existing post |
| `post/<int:pk>/delete/` | post_delete | Delete post |
| `posts/` | post_list | List all posts |
| `category/<slug:category_slug>/` | category_posts | List posts by category |
| `tag/<slug:tag_slug>/` | tag_posts | List posts by tag |
| `search/` | search_posts | Search posts |

- Interactions App URLs

| URL Pattern | View Name | Description |
|-------------|-----------|-------------|
| `post/<int:pk>/comment/` | add_comment | Add comment to post |
| `comment/<int:pk>/reply/` | add_reply | Reply to comment |
| `comment/<int:pk>/edit/` | edit_comment | Edit comment |
| `comment/<int:pk>/delete/` | delete_comment | Delete comment |
| `post/<int:pk>/like/` | like_post | Like/unlike post |
| `post/<int:pk>/bookmark/` | bookmark_post | Bookmark/unbookmark post |
| `notifications/` | notifications | View user notifications |

## 3. 프로젝트 구조와 개발 일정
### 3.1 프로젝트 구조
### 3.2 개발 일정(WBS)
```mermaid
gantt
    title 프로젝트 일정
    dateFormat  YYYY-MM-DD
    section 8월 26일
    프로젝트 기획           :a1, 2024-08-26, 1d
    WBS 작성                :a2, 2024-08-26, 1d
    ERD 작성                :a3, 2024-08-26, 1d
    URL 설계                :a4, 2024-08-26, 1d
    모델 설계               :a5, 2024-08-26, 1d

    section 8월 27일 ~ 29일
    CRUD 구현               :b1, 2024-08-27, 3d
    인증 구현               :b2, 2024-08-27, 3d
    회원 관련 기능 구현     :b3, 2024-08-27, 3d
    댓글 구현               :b4, 2024-08-27, 3d
    부가 기능 구현          :b5, 2024-08-27, 3d

    section 8월 30일
    와이어프레임            :c1, 2024-08-30, 1d
    기획서 마무리          :c2, 2024-08-30, 1d
    웹페이지 배포          :c3, 2024-08-30, 1d
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
