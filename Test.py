from BeautifulSoup import BeautifulStoneSoup as Soup

xml = """
<TrdCaptRpt RptID="10000001" TransTyp="0">
    <RptSide Side="1" Txt1="XXXXX">
        <Pty ID="XXXXX" R="1"/>
    </RptSide>
</TrdCaptRpt>
"""

soup = Soup(xml)
rpt_side = soup.trdcaptrpt.rptside
rpt_side['txt1'] = 'Updated'
rpt_side.pty['id'] = 'Updated'

print soup