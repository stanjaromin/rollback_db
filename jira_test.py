from jira import JIRA

jira = JIRA('https://tiswebmaintenance.atlassian.net/')
auth_jira = JIRA(basic_auth=('maintenance_dmm@globallogic.com', '#####'))

issue = jira.issue('TED-85')
print(issue.fields.project.key)           # 'JRA'
print(issue.fields.issuetype.name)          # 'New Feature'
print(issue.fields.reporter.displayName)    # 'Mike Cannon-Brookes [Atlassian]'