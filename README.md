# Django를 활용한 블로그 프로젝트
## WBS

```mermaid
graph TD
    A[프로젝트 시작] --> B[8월 26일]
    B --> B1[프로젝트 기획]
    B --> B2[WBS 작성]
    B --> B3[ERD 작성]
    B --> B4[URL 설계]
    B --> B5[모델 설계]

    A --> C[8월 27일 ~ 29일]
    C --> C1[CRUD 구현]
    C --> C2[인증 구현]
    C --> C3[회원 관련 기능 구현]
    C --> C4[댓글 구현]
    C --> C5[부가 기능 구현]

    A --> D[8월 30일]
    D --> D1[와이어프레임]
    D --> D2[기획서 마무리]
    D --> D3[웹페이지 배포]

    classDef milestone fill:#f9f,stroke:#333,stroke-width:2px;
    class A milestone;
```

