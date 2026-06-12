# 1.5.	보고서

회계 모듈에서 모든 회계 데이터가 처리된 후, 사용자는 다음과 같은 보고서를 생성할 수 있습니다.

&#x20;

#### 1.5.1.   시간표

·         회계기간 선택(기산일 \~ 마감일)

·         통화 단위 선택(Currency ID)

·         출력 방식 선택:

&#x20;          §  화면에서 직접 조회 **(조회)**

&#x20;          §  PDF 형식으로 보고서 인쇄 **(PDF 인쇄)**

&#x20;          §  Excel 파일로 내보내기 **(엑셀 내보내기)**

<figure><img src="../.gitbook/assets/image (94).png" alt=""><figcaption></figcaption></figure>

채권채무 계정(131, 331, 138, 338)이 아닌 계정을 더블 클릭하면, 계정에 따라 명세서가 표시됩니다.

<figure><img src="../.gitbook/assets/image (95).png" alt=""><figcaption></figcaption></figure>

채권채무 계정(131, 331, 138, 338)을 더블 클릭하면, 대상처별 채권채무 내역이 표시됩니다.

<figure><img src="../.gitbook/assets/image (96).png" alt=""><figcaption></figcaption></figure>

대상자별 채권채무 상세내역이 포함된 시산표를 출력할 경우, 해당 채권채무 계정(131, 331, 138, 338)을 더블 클릭한 후 엑셀로 내보내기를 선택합니다.

<figure><img src="../.gitbook/assets/image (97).png" alt=""><figcaption></figcaption></figure>

#### 1.5.2.   총계정원장

·         회계기간 선택(기산일 \~ 마감일)

·         통화 단위 선택(Currency ID)

·         출력 계정 유형 선택(Option)

&#x20;               §  전체

&#x20;               §  특정 계정(계정 번호를 선택하여 F3 누르기)

PDF 형식으로 **보고서 인쇄**, 또는 **Excel 파일로** 내보내기 선택

<figure><img src="../.gitbook/assets/image (98).png" alt=""><figcaption></figcaption></figure>

전체 계정(All)을 선택하여 엑셀 내보내기:

·         Sheet DOCSMAP: 보고서 엑셀 파일에 포함된 상세 계정 목록

·         확인할 시트로 연결하기 위한 계정 클릭

·         각 상세 엑셀 시트상: DOCSMAP 시트로 돌아가기 위해 DOCSMAP(B10 셀) 클릭

&#x20;

#### 1.5.3.   상세 총계정원장

·         회계기간 선택(기산일 \~ 마감일)

·         통화 단위 선택(Currency ID)

·         출력 계정 유형 선택(Option)

&#x20;             §  전체

&#x20;             §  특정 계정(계정 번호를 선택하여 F3 누르기)

·         보고서 선택

PDF 형식으로 보고서 인쇄, 또는 Excel 파일로 내보내기 선택

<figure><img src="../.gitbook/assets/image (99).png" alt=""><figcaption></figcaption></figure>

\-   **GLDetail** 보고서를 내보내는 경우

·         Sheet Index: 보고서 엑셀 파일에 포함된 상세 계정 목록

·         계정을 클릭하여 조회 시트로 이동

·         각 상세 엑셀 시트상: Index 시트로 돌아가기 위해 DOCSMAP(B10 셀) 클릭

\-    **GLDetail Main Account** 보고서를 내보내는 경우: 상위(메인) 계정 기준으로 보고서를 확인합니다.

\-     **전체 보고서를** 내보내는 경우: GLDetail 보고서 내보내기와 동일하나 대차대조표(BS), 시산표(TB), 손익계산서(PL) 가 추가로 포함됩니다.

<figure><img src="../.gitbook/assets/image (100).png" alt=""><figcaption></figcaption></figure>

#### 1.5.4.   대차대조표

·         회계기간 선택(기산일 \~ 마감일)

·         통화 단위 선택(Currency ID)

·         화면에서 보기, PDF 형식으로 보고서 인쇄, 또는 Excel 파일로 내보내기 선택

<figure><img src="../.gitbook/assets/image (101).png" alt=""><figcaption></figcaption></figure>

**상세보기 버튼**: 각 지표의 데이터가 어떤 계정에서 가져왔는지를 표시합니다.

<figure><img src="../.gitbook/assets/image (102).png" alt=""><figcaption></figcaption></figure>

**엑셀로 내보내기** 버튼: 다음과 같은 선택으로 보고서를 엑셀로 내보내기

·         상세: 상세 계정의 지표 정보를 포함한 엑셀 파일로 내보내기

·         종합: 지표만 포함된 엑셀 파일로 내보내기

**인쇄** 버튼: 보고서 인쇄

·         집계형 데이터 그리드의 경우: 집계된 수치 기준으로 인쇄

·         상세 데이터 그리드의 경우: 계정의 상세 수치가 포함된 보고서 인쇄



#### 1.5.5.   손익계산서

·         회계기간 선택(기산일 \~ 마감일)

·         통화 단위 선택(Currency ID)

·         화면에서 보기, PDF 형식으로 보고서 인쇄, 또는 Excel 파일로 내보내기 선택

<figure><img src="../.gitbook/assets/image (103).png" alt=""><figcaption></figcaption></figure>

**상세보기 버튼**: 각 지표의 데이터가 어떤 계정에서 가져왔는지를 표시합니다.

**엑셀로 내보내기 버튼**: 다음과 같은 선택으로 보고서를 엑셀로 내보내기

·         상세: 상세 계정의 지표 정보를 포함한 엑셀 파일로 내보내기

·         종합: 지표만 포함된 엑셀 파일로 내보내기

**인쇄** 버튼: 보고서 인쇄

·         집계형 데이터 그리드의 경우: 집계된 수치 기준으로 인쇄

·         상세 데이터 그리드의 경우: 계정의 상세 수치가 포함된 보고서 인쇄

<figure><img src="../.gitbook/assets/image (104).png" alt=""><figcaption></figcaption></figure>

#### 1.5.6.   현금흐름표

·         회계기간 선택(기산일 \~ 마감일)

·         계산법: 직접법 또는 간접법

·         PDF 형식으로 보고서 인쇄 또는 Excel 파일로 내보내기 선택

<figure><img src="../.gitbook/assets/image (105).png" alt=""><figcaption></figcaption></figure>

#### 1.5.7.   일일시간표

·         회계기간 선택(기산일 \~ 마감일)

·         PDF 형식으로 보고서 인쇄 또는 Excel 파일로 내보내기 선택

#### 1.5.8.   제조 원가 명세서

·         회계기간 선택(기산일 \~ 마감일)

·         PDF 형식으로 보고서 인쇄 또는 Excel 파일로 내보내기 선택

&#x20;

#### 1.5.9.   비제조 원가 명세서

·         회계기간 선택(기산일 \~ 마감일)

·         PDF 형식으로 보고서 인쇄 또는 Excel 파일로 내보내기 선택

&#x20;

#### 1.5.10.   상세 제조 원가 명세서

·         회계기간 선택(기산일 \~ 마감일)

·         비교기간 선택(기산일 \~ 마감일)

·         PDF 형식으로 보고서 인쇄 또는 Excel 파일로 내보내기 선택

&#x20;

#### 1.5.11.   일반 분개장

·         기간 선택(기산일 \~ 마감일)

·         PDF 형식으로 보고서 인쇄 또는 Excel 파일로 내보내기 선택

&#x20;

#### 1.5.12.   회계/ 출금/ 입금 전표 출력

·         기간 선택(기산일 \~ 마감일)

·         PDF 형식으로 보고서 인쇄 또는 Excel 파일로 내보내기 선택

&#x20;

#### 1.5.13.   자동대체분개

·         기간 선택(기산일 \~ 마감일)

PDF 형식으로 보고서 인쇄 또는 Excel 파일로 내보내기 선택
