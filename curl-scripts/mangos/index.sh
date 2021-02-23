#!/bin/bash

curl "http://localhost:8000/posts/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
