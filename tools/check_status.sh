#!/bin/bash
echo "=== EPSTEIN FILES ANALYSIS STATUS ==="
echo ""

# OCR Status
if [ -f "/atb-data/rye/dump/epstein_files/ocr_database.db" ]; then
    OCR_COUNT=$(sqlite3 /atb-data/rye/dump/epstein_files/ocr_database.db "SELECT COUNT(*) FROM ocr_results WHERE ocr_text IS NOT NULL" 2>/dev/null || echo "0")
    echo "📝 OCR: $OCR_COUNT / 38955 images processed"
else
    echo "📝 OCR: Database not yet created"
fi

# Redaction Status
if [ -f "/atb-data/rye/dump/epstein_files/redaction_analysis.db" ]; then
    REDACT_COUNT=$(sqlite3 /atb-data/rye/dump/epstein_files/redaction_analysis.db "SELECT COUNT(*) FROM redactions" 2>/dev/null || echo "0")
    REDACTED=$(sqlite3 /atb-data/rye/dump/epstein_files/redaction_analysis.db "SELECT COUNT(*) FROM redactions WHERE has_redaction=1" 2>/dev/null || echo "0")
    echo "🔲 Redaction detector: $REDACT_COUNT scanned, $REDACTED with redactions found"
else
    echo "🔲 Redaction detector: Database not yet created"
fi

# Qwen2-VL Status
if [ -f "/atb-data/rye/dump/epstein_files/image_analysis.db" ]; then
    QWEN_COUNT=$(sqlite3 /atb-data/rye/dump/epstein_files/image_analysis.db "SELECT COUNT(*) FROM images WHERE analysis_text IS NOT NULL AND length(analysis_text) > 0" 2>/dev/null || echo "0")
    echo "🤖 Qwen2-VL: $QWEN_COUNT images analyzed"
else
    echo "🤖 Qwen2-VL: Database not found"
fi

# Evidence findings
FINDINGS=$(wc -l < /atb-data/rye/dump/epstein_files/evidence_findings.jsonl 2>/dev/null || echo "0")
echo "📋 Manual findings logged: $FINDINGS"

# Cross-references
if [ -f "/atb-data/rye/dump/epstein_files/name_crossref.jsonl" ]; then
    XREF=$(wc -l < /atb-data/rye/dump/epstein_files/name_crossref.jsonl)
    echo "🔗 Name cross-references: $XREF"
fi

# Priority documents
if [ -f "/atb-data/rye/dump/epstein_files/priority_documents.jsonl" ]; then
    PRIORITY=$(wc -l < /atb-data/rye/dump/epstein_files/priority_documents.jsonl)
    echo "⚠️  Priority documents flagged: $PRIORITY"
fi

echo ""
echo "Running processes:"
ps aux | grep -E "(bulk_ocr|redaction_detector|comprehensive_image|dependent_analysis)" | grep -v grep | awk '{print "  " $11 " " $12}'
