from client import MetaMuseMultiAppPlannerClient
client = MetaMuseMultiAppPlannerClient()
print(client.plan_steps(["Gmail", "Slack"], "Forward summaries"))