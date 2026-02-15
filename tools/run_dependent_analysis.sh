#!/bin/bash
# Wait for OCR to process enough documents, then run dependent analysis

OCR_DB="/atb-data/rye/dump/epstein_files/ocr_database.db"
MIN_DOCS=5000

echo "Waiting for OCR to process at least $MIN_DOCS documents..."

while true; do
    if [ -f "$OCR_DB" ]; then
        COUNT=$(sqlite3 "$OCR_DB" "SELECT COUNT(*) FROM ocr_results WHERE ocr_text IS NOT NULL" 2>/dev/null || echo "0")
        echo "$(date): OCR has processed $COUNT documents"
        
        if [ "$COUNT" -ge "$MIN_DOCS" ]; then
            echo "Threshold reached! Running dependent analysis..."
            break
        fi
    fi
    sleep 60
done

cd /atb-data/rye/dump/epstein_files

echo "Running name search..."
python3 tools/name_search.py

echo "Running document classifier..."
python3 tools/document_classifier.py

echo "Building knowledge graph..."
python3 tools/knowledge_graph.py

echo "All analysis complete!"
