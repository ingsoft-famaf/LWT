from StringIO import StringIO

VALIDATOR = StringIO('''\
<xs:schema attributeFormDefault="unqualified" elementFormDefault="qualified" xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:element name="subject" type="subjectType"/>
  <xs:complexType name="questionType">
    <xs:sequence>
      <xs:element type="xs:string" name="tanswer"/>
      <xs:element type="xs:string" name="answer" maxOccurs="2" minOccurs="2"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="topicType">
    <xs:sequence>
      <xs:element type="questionType" name="question" maxOccurs="unbounded" minOccurs="1"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="subjectType">
    <xs:sequence>
      <xs:element type="topicType" name="topic" maxOccurs="unbounded" minOccurs="1"/>
    </xs:sequence>
  </xs:complexType>
</xs:schema>
''')
