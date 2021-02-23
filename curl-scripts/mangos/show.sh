#!/bin/bash

curl "http://localhost:8000/posts/${ID}" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
