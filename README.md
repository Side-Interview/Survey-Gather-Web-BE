# Survey-Gather-Django-BE

<!-- toc -->
## 목차
- [Survey-Gather-Django-BE](#survey-gather-django-be)
  - [목차](#목차)
  - [기술 스택](#기술-스택)
  - [Git Branch/Commit](#git-branchcommit)
    - [Branch 운영 정책](#branch-운영-정책)
    - [Git Commit Message 정책](#git-commit-message-정책)
    - [Commit Message Template 적용](#commit-message-template-적용)
    - [pre-commit 적용](#pre-commit-적용)
  - [로컬 환경 설정](#로컬-환경-설정)
    - [Step1: 환경설정 및 패키지 설치](#step1-환경설정-및-패키지-설치)
    - [Step2: Local Server 실행](#step2-local-server-실행)

<!-- tocstop -->
## 기술 스택
- [Python 3.11](https://www.python.org/)
- [Django 4.2.5](https://docs.djangoproject.com/ko/4.2/intro/)
- [Django Rest Framework 3.14.0](https://www.django-rest-framework.org/)
- [Git](https://git-scm.com/docs)
- [Github Actions](https://docs.github.com/ko/actions)


## Git Branch/Commit
### Branch 운영 정책

- master : 라이브 서버에 제품으로 **출시**되는 브랜치
- develop : 다음 출시 버전을 대비하여 **개발**하는 브랜치
- feature : **추가 기능** 개발 브랜치. develop 브랜치에 들어간다.
- release : **다음 버전** 출시를 준비하는 브랜치
    - develop 브랜치를 release 브랜치로 옮긴 후 QA, 테스트를 진행하고 master 브랜치로 합친다.
- hotfix : master 브랜치에서 발생한 **버그를 수정**하는 브랜치. (사용하지 않기로 함)
- F ➝ D ➝ R ➝ M ➝ H

### Git Commit Message 정책
```
커밋 메시지의 7가지 규칙

- 제목과 본문을 빈 행으로 구분한다.
- 제목은 50글자 이내로 제한한다.
- 제목의 첫 글자는 대문자로 작성한다.
- 제목 끝에는 마침표를 넣지 않는다.
- 제목은 명령문으로 사용하며 과거형을 사용하지 않는다.
- 본문의 각 행은 72글자 내로 제한한다.
- 어떻게 보다는 무엇과 왜를 설명한다.
```
**커밋 메시지 구조**

```
// Header, Body, Footer는 빈 행으로 구분한다.
타입(스코프): 주제(제목) // Header(헤더)

본문 // Body(바디)

바닥글 // Footer
```

| 타입 이름 | 내용 |
| --- | --- |
| feat | 새로운 기능에 대한 커밋 |
| fix | 버그 수정에 대한 커밋 |
| build | 빌드 관련 파일 수정 / 모듈 설치 또는 삭제에 대한 커밋 |
| chore | 그 외 자잘한 수정에 대한 커밋 |
| ci | ci 관련 설정 수정에 대한 커밋 |
| docs | 문서 수정에 대한 커밋 |
| style | 코드 스타일 혹은 포맷 등에 관한 커밋 |
| refactor | 코드 리팩토링에 대한 커밋 |
| test | 테스트 코드 수정에 대한 커밋 |
| perf | 성능 개선에 대한 커밋 |

[작성 예시 참고](https://tinyurl.com/yrmvw4fo)

### [Commit Message Template 적용](https://velog.io/@bky373/Git-%EC%BB%A4%EB%B0%8B-%EB%A9%94%EC%8B%9C%EC%A7%80-%ED%85%9C%ED%94%8C%EB%A6%BF)
- 커밋의 일관성을 위해 커밋 메시지 템플릿을 적용합니다.
```bash
git config --local commit.template .gitmessage.txt
git add .
git commit
```

### [pre-commit 적용](https://www.daleseo.com/pre-commit/)
- 코드의 일관성을 위해 pre-commit을 적용합니다.
```bash
poetry run pre-commit install
git commit
```
## 로컬 환경 설정
### Step1: 환경설정 및 패키지 설치
```bash
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt # poetry install
poetry install
```

### Step2: Local Server 실행
```bash
poetry run python manage.py runserver --settings=config.django.local # local 환경 실행
```
