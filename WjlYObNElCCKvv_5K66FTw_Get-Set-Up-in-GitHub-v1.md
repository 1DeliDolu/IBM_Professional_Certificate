<script>
  const base_url = "https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL1dqbFlPYk5FbENDS3Z2XzVLNjZGVHcvR2V0LVNldC1VcC1pbi1HaXRIdWItdjEubWQ_dD0xNzQ2MTI0NjQ5IiwidG9vbF90eXBlIjoiaW5zdHJ1Y3Rpb25hbC1sYWIiLCJhdGxhc19maWxlX2lkIjo1Mjc1MiwiYWRtaW4iOmZhbHNlLCJpYXQiOjE3NTc2OTU3NTV9.2bPL-aJzDN9sA3ZrrMcx5tF5ofD93QASYaeiKNYL2SY";
  const currentUrl = new URL(window.location.href);
  const targetUrl = new URL(base_url);
  const langParam = currentUrl.searchParams.get('lang');
  if (langParam) {
    targetUrl.searchParams.set('lang', langParam);
  }
  window.location.href = targetUrl.toString();
</script>
