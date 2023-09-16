import re
items = ['11번가(com.elevenst) v8.2.1', '11번가(com.elevenst) v8.3.4', 'CJMall(com.cjoshppingphone) 6.7.3v', 'G9(com.ebay.kr.g9) v6.3.1', 'GS SHOP(gsshop.mobile.v2) 6.4.7v', 'Gmarket(com.ebay.kr.gmarket) v9.0.0', 'LFMall(kr.co.lgfashion.lgfashionshop.v28) 3.8.1', 'Tmon(com.tmon) 5.1.7.1', '당근마켓(com.towneers.www) 5.5.0', '데상트 코리아 Eshop(kr.co.descentekorea.eshop) 1.1.0(1100)', '롯데마트 M쿠폰(com.lottemart.lmscp) v3.0.4', '롯데면세점(com.lotte.lottedutyfree) v7.0.19', '롯데홈쇼핑(com.omnitel.android.lottewebview) v3.2.4', '번개장터(kr.co.quicket) 5.30.4버전', '쇼킹딜(com.elevenst.deals) 4.3.3', '여기어때(kr.goodchoice.abouthere) 3.30.12(33012)', '여성쇼핑몰 모음 지그재그(com.croquis.zigzag) v5.11.1', '옥션(com.ebay.kr.auction) v7.9.0', '요기요(com.fineapp.yogiyo) v5.3.1', '인터파크(com.interpark.shop) v4.0.5', '중고나라(com.elz.secondhandstore) 6.7.9', '지그재그(com.croquis.zigzag) 6.7.1v', '지니뮤직(com.ktmusic.geniemusic) 04.07.01(4070103)', '코오롱몰(com.kolon.kolonmall) v2.1.12(47)', '쿠팡(com.coupang.mobile) v5.7.2', '쿠팡(com.coupang.mobile) v5.9.4', '할인중독(com.jasonmg.salepoison) v2.3.0(44)', '해피포인트 v6.4.3', '해피포인트 v6.5.11', '현대Hmall(com.hmallapp) v5.10.9', '홈앤쇼핑(com.hnsmall) 3.2.1v']

for x in items:
    x = re.sub(r'\([^)]*\)', '', x)
    data = """---
layout: default
title: %s
parent: 취약점 공개
---

아직 작성되지 않았습니다."""%(x)
    open(x+".md", 'w').write(data)
