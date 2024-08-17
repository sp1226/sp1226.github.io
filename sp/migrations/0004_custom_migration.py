from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('sp', '0003_employee'),
    ]

    operations = [
        migrations.RunSQL(
            """
            CREATE TABLE IF NOT EXISTS sp_product (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL
            );
            """
        ),
    ]
