# DEMO


## Test data

    jsonschema -i data/1answer.json schema-compiled-reduced.json
    jsonschema -i data/2answer-bad-category-and-sub-category.json schema-compiled-reduced.json
    jsonschema -i data/2answer-bad-sub-category-and-sub-category.json schema-compiled-reduced.json
    jsonschema -i data/2answer-good-diff-categories.json schema-compiled-reduced.json
    jsonschema -i data/2answer-good-diff-sub-categories.json schema-compiled-reduced.json

    jsonschema -i data/1answer.json schema-compiled.json
    jsonschema -i data/2answer-bad-category-and-sub-category.json schema-compiled.json
    jsonschema -i data/2answer-bad-sub-category-and-sub-category.json schema-compiled.json
    jsonschema -i data/2answer-good-diff-categories.json schema-compiled.json
    jsonschema -i data/2answer-good-diff-sub-categories.json schema-compiled.json