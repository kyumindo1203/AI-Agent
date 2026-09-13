# 에이전트 계층

이 디렉터리는 워크스페이스의 추상 에이전트 계층을 정의한다.

구조는 다음과 같다.

- agents/
  - secretary/ : 사용자 인터페이스 에이전트
  - orchestrator/ : 작업 조율 계층
    - children/ : 오케스트레이터의 하위 전문 에이전트 집합
      - planner/
      - researcher/
      - developer/
      - tester/
      - reviewer/
      - security/

각 역할 디렉터리는 다음 구조로 나뉜다.

- agent/ : 에이전트 객체 설명과 런타임 계약
- memory/ : 에이전트 메모리 저장 영역
- metadata.yaml : 계층 메타데이터

현재 설계는 config/agent_roles.yaml의 역할 레지스트리를 따른다. 상위 오케스트레이터는 전문 에이전트들을 하위 자식 계층으로 관리한다.
