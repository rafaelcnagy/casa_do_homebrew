MAX_UPLOAD_SIZE = 5  # em mb
VALID_EXTENSIONS = ['.pdf', '.doc', '.docx', '.xlsx', '.xls']


def validate_file_extension(file):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(file.name)[1]  # [0] returns path+filename
    if not ext.lower() in VALID_EXTENSIONS:
        raise ValidationError('Formato de arquivo não suportado.')


def validate_file_size(file):
    from django.core.exceptions import ValidationError
    file_size = file.size
    if file_size >= 5 * 1024 * 1024:
        raise ValidationError(f'Tamanho excedeu o limite de {MAX_UPLOAD_SIZE} MB.')

