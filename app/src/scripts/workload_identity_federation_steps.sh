gcloud iam workload-identity-pools create "github" \
  --project="zdsdatamatch00" \
  --location="global" \
  --display-name="GitHub Actions Pool"

gcloud iam workload-identity-pools describe "github" \
  --project="zdsdatamatch00" \
  --location="global" \
  --format="value(name)"

gcloud iam workload-identity-pools providers create-oidc "my-repo" \
  --project="zdsdatamatch00" \
  --location="global" \
  --workload-identity-pool="github" \
  --display-name="My GitHub repo Provider" \
  --attribute-mapping="google.subject=assertion.sub,attribute.actor=assertion.actor,attribute.repository=assertion.repository,attribute.repository_owner=assertion.repository_owner" \
  --attribute-condition="assertion.repository_owner == 'liamk-zds'" \
  --issuer-uri="https://token.actions.githubusercontent.com"