# myLabs
- 혼자 이것저것 프로그램을 만들거나

- 프로그래밍 공부에 대한 방향성 잡는 공간







## 프로그램

#### autoClick

- 자동으로 클릭해주는 프로그램





## Study

#### on-premise

- 클라우드를 사용하는 것이 아닌 기업 내부에서 서버를 직접 관리하고 운용
- 반대 개념이 클라우드





### Cloud Native 를 위한 주요 4가지 요소

#### 1. CI/CD

- **CI** : Continuous Integration / 지속적인 통합
  - 애플리케이션에서 신규코드 변경 사항이 정기적으로 빌드 및 테스트가 되고, 이를 공유 레포지토리에 통합하는 것을 의미 (동기화와 비슷한 방식)
  - 필요 조건
    - MSA (Micro Service Archietecture) : 아키텍처 모델로서 작은 기능으로 서비스를 잘게 쪼개어서 개발하는 형태로 아키텍처에서 특정기능만을 따로 배포할 수 있다는  장점이 있다
    - Agile : 소규모 기능 단위로 빠르게 개발하고 적용을 반복하는 개발 방법
    - 형상관리 툴 :  Git, SVN 등
- **CD** : Continuous Delivery or Deployment / 지속적 서비스 제공 또는 배포
  - Continuous Delivery : 공유 레포지토리 자동 배포
  - Continuous Deployment : Production 레벨까지 자동 배포
- CI 가 새로운 소스코드의 빌드, 테스트, 병합을 의미하면 CD 는 Repository ~ Production  환경까지 배포되는 것
- 예시로는 Git을 이용한 Master Branch를 만들고 이 Branch에 개발자들 각자 Branch의 Code를 Merge하는 것부터 시작한다



#### 2. DevOps

- 애플리케이션 개발-운영 간의 협업 프로세스를 자동화하는 것을 말하며, 결과적으로 애플리케이션의 개발과 개선 속도를 빠르게 한다



#### 3. 컨테이너 기반 인프라

- 시스템을 가상화하는 것이 아니라 애플리케이션을 구동할 수 있는 컴퓨팅 작업을 패키징하여 가상화 한것



#### 4. Microservice

- 애플리케이션을 구성하는 서비스들을 독립적인 작은 단위로 분해하여 구축하고 각 구성 요소들을 네트워크로 통신하는 아키텍처
- 서비스 안정성과 확장성(scaling)을 지원





### K8S study

- Kubernetes up&Running 책으로 진행
- 기본적인 내용파악하는데 도움







### daily

---

#### 0222

- kubernetes up&running
- node.js 프로그래밍



#### 0303

- setting up system
- 네트워크 아직 설치 안됨



#### 0307

- 5G 실험테이블 구성하기
  - 모니터3, 베어본3, 카메라2
  - Q
    - 카메라 ip가 무선이었는지...?
    - 베어본ip 는 무선사용 및 유선은 강제로 사용시에만 연결가능하게 했었던듯