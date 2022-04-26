class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emailSet = set()
        for email in emails:
            uniqEmail = self.simplifyEmail(email)
            emailSet.add(uniqEmail)
        return len(emailSet)
    
    def simplifyEmail(self, email):
        localName, domainName = email.split('@')
        localName = localName.replace('.','')
        plusLocation = localName.find('+')
        if plusLocation != -1:
            localName = localName[:plusLocation]
        return localName + '@' + domainName