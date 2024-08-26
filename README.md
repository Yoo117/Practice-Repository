# Django를 활용한 블로그 프로젝트입니다.

erDiagram
    User ||--o{ Post : "작성"
    User ||--o{ Comment : "작성"
    User ||--|| Profile : "가짐"
    User ||--o{ SearchHistory : "검색"
    User ||--o{ Like : "좋아요"
    Post ||--o{ Comment : "포함"
    Post }o--o{ Tag : "태그"
    Post ||--o{ Like : "받음"
    
    User {
        int id PK
        string password
        string nickname
        string email
        string profile_image
    }
    
    Post {
        int id PK
        string title
        text content
        int author FK
        datetime created_at
        datetime updated_at
        string head_image
        int view_count
    }
    
    Comment {
        int id PK
        int post FK
        int author FK
        text content
        datetime created_at
        int parent FK
    }
    
    Tag {
        int id PK
        string name
        datetime created_at
    }
    
    Profile {
        int id PK
        int user FK
        text bio
        string profile_image
        date birthdate
    }
    
    SearchHistory {
        int id PK
        int user FK
        string query
        datetime searched_at
    }
    
    Like {
        int id PK
        int user FK
        int post FK
        datetime created_at
    }
