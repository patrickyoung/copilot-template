# Prompt Generator Service

## Purpose
To process a JSON file containing markdown-formatted text and generate a concise, useful, and well-written prompt for a language model like GPT.

## Endpoint Specification

1. Endpoint: /generate-prompt
2. Method: POST
3. Request Body:
- application/json
- Structure: { "markdownText": "string" }
- Description: Contains markdown-formatted text as a string.

## Processing Logic
- The service will parse the JSON to extract markdown content.
- It will analyze the markdown to identify key themes, actions, or questions.
- Based on the analysis, it will construct a prompt suitable for a language model.

## Response Format

- Success Response:
  - Code: 200 OK
  -Content: { "prompt": "string" } - A well-structured prompt derived from the markdown text.

- Error Responses:
  - Invalid JSON: 400 Bad Request
  - Markdown Parsing Error: 422 Unprocessable Entity
  - Internal Server Error: 500 Internal Server Error

## OpenAPI Specification
'''yaml
openapi: 3.0.0
info:
  title: Markdown to Prompt Generator
  version: 1.0.0
paths:
  /generate-prompt:
    post:
      summary: Generates a prompt from markdown text
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                markdownText:
                  type: string
                  description: Markdown-formatted text.
            example:
              markdownText: "# Title\nSome content here..."
      responses:
        '200':
          description: Successfully generated prompt
          content:
            application/json:
              schema:
                type: object
                properties:
                  prompt:
                    type: string
                    description: Generated prompt for a language model.
        '400':
          description: Invalid JSON format
        '422':
          description: Error in parsing markdown
        '500':
          description: Internal server error
'''