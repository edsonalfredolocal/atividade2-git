
#!/bin/bash
echo "===== SCRIPT AVANÇADO ====="

echo "Data atual:"
date

echo ""
echo "Número de ficheiros na pasta:"
ls | wc -l

echo ""
echo "A criar ficheiro de log..."

echo "Log criado em: $(date)" >> log.txt
echo "Total de ficheiros: $(ls | wc -l)" >> log.txt

echo ""
echo "Log atualizado com sucesso!"