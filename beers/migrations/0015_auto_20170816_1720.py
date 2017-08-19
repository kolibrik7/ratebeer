# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-16 17:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('beers', '0014_auto_20170814_1738'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brewery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brewery', models.CharField(max_length=50)),
                ('country', models.CharField(choices=[('AF', 'Afganistan'), ('AL', 'Albánsko'), ('DZ', 'Alžírsko'), ('AD', 'Andorra'), ('AO', 'Angola'), ('AI', 'Anguilla'), ('AG', 'Antigua a Barbuda'), ('AR', 'Argentína'), ('AM', 'Arménsko'), ('AW', 'Aruba'), ('AU', 'Austrália'), ('AZ', 'Azerbajdžan'), ('BS', 'Bahamy'), ('BH', 'Bahrajn'), ('BD', 'Bangladéš'), ('BB', 'Barbados'), ('BE', 'Belgicko'), ('BZ', 'Belize'), ('BJ', 'Benin'), ('BM', 'Bermudy'), ('BT', 'Bhután'), ('BY', 'Bielorusko'), ('BO', 'Bolívia'), ('BQ', 'Bonaire, Svätý Eustach a Saba'), ('BA', 'Bosna a Hercegovina'), ('BW', 'Botswana'), ('BV', 'Bouvetov ostrov'), ('BR', 'Brazília'), ('VG', 'Britské Panenské ostrovy'), ('BN', 'Brunej'), ('BG', 'Bulharsko'), ('BF', 'Burkina'), ('BI', 'Burundi'), ('CK', 'Cookove ostrovy'), ('CW', 'Curacao'), ('CY', 'Cyprus'), ('TD', 'Čad'), ('CZ', 'Česká republika'), ('ME', 'Čierna Hora'), ('CL', 'Čile'), ('CN', 'Čína'), ('DK', 'Dánsko'), ('DM', 'Dominika'), ('DO', 'Dominikánska republika'), ('DJ', 'Džibutsko'), ('EG', 'Egypt'), ('EC', 'Ekvádor'), ('ER', 'Eritrea'), ('EE', 'Estónsko'), ('ET', 'Etiópia'), ('FO', 'Faerské ostrovy'), ('FK', 'Falklandy'), ('FJ', 'Fidži'), ('PH', 'Filipíny'), ('FI', 'Fínsko'), ('FR', 'Francúzsko'), ('GA', 'Gabon'), ('GM', 'Gambia'), ('GH', 'Ghana'), ('GI', 'Gibraltár'), ('GR', 'Grécko'), ('GD', 'Grenada'), ('GL', 'Grónsko'), ('GE', 'Gruzínsko'), ('GT', 'Guatemala'), ('GG', 'Guernsey'), ('GN', 'Guinea'), ('GW', 'Guinea-Bissau'), ('GY', 'Guyana'), ('HT', 'Haiti'), ('NL', 'Holandsko'), ('HN', 'Honduras'), ('HK', 'Hongkong'), ('HR', 'Chorvátsko'), ('IN', 'India'), ('ID', 'Indonézia'), ('XX', 'Iné'), ('IQ', 'Irak'), ('IR', 'Irán'), ('IS', 'Island'), ('IL', 'Izrael'), ('IE', 'Írsko'), ('JM', 'Jamajka'), ('JP', 'Japonsko'), ('YE', 'Jemen'), ('JE', 'Jersey'), ('JO', 'Jordánsko'), ('ZA', 'Južná Afrika'), ('GS', 'Južná Georgia a JužnéSandwichove ostrovy'), ('SS', 'Južný Sudán'), ('KY', 'Kajmanie ostrovy'), ('KH', 'Kambodža'), ('CM', 'Kamerun'), ('CA', 'Kanada'), ('CV', 'Kapverdy'), ('QA', 'Katar'), ('KZ', 'Kazachstan'), ('KE', 'Keňa'), ('KG', 'Kirgizsko'), ('KI', 'Kiribati'), ('CO', 'Kolumbia'), ('KM', 'Komory'), ('CD', 'Kongo (býv. Zair)'), ('CG', 'Kongo'), ('KR', 'Kórejská republika'), ('KP', 'Kórejská ľudovodemokratická republika (KĽDR)'), ('CR', 'Kostarika'), ('CU', 'Kuba'), ('KW', 'Kuvajt'), ('LA', 'Laos'), ('LS', 'Lesotho'), ('LB', 'Libanon'), ('LR', 'Libéria'), ('LY', 'Líbya'), ('LI', 'Lichtenštajnsko'), ('LT', 'Litva'), ('LV', 'Lotyšsko'), ('LU', 'Luxembursko'), ('MO', 'Macao'), ('MK', 'Macedónsko'), ('MG', 'Madagaskar'), ('MY', 'Malajzia'), ('MW', 'Malawi'), ('MV', 'Maldivy'), ('ML', 'Mali'), ('MT', 'Malta'), ('IM', 'Man'), ('MA', 'Maroko'), ('MU', 'Maurícius'), ('MR', 'Mauritánia'), ('HU', 'Maďarsko'), ('MX', 'Mexiko'), ('MM', 'Mjanmarsko'), ('MD', 'Moldavsko'), ('MC', 'Monako'), ('MN', 'Mongolsko'), ('MS', 'Montserrat'), ('MZ', 'Mozambik'), ('NA', 'Namíbia'), ('NR', 'Nauru'), ('DE', 'Nemecko'), ('NP', 'Nepál'), ('NE', 'Niger'), ('NG', 'Nigéria'), ('NI', 'Nikaragua'), ('NO', 'Nórsko'), ('NZ', 'Nový Zéland'), ('OM', 'Omán '), ('PK', 'Pakistan'), ('PW', 'Palau'), ('PA', 'Panama'), ('PG', 'Papua-Nová Guinea'), ('PY', 'Paraguaj'), ('PE', 'Peru'), ('CI', 'Pobrežie Slonoviny'), ('PL', 'Poľsko'), ('PT', 'Portugalsko'), ('AT', 'Rakúsko'), ('GQ', 'Rovníková Guinea'), ('RO', 'Rumunsko'), ('RU', 'Ruská federácia'), ('RW', 'Rwanda'), ('SV', 'Salvádor'), ('WS', 'Samoa'), ('SM', 'San Maríno'), ('SA', 'Saudská Arábia'), ('SN', 'Senegal'), ('MP', 'Severné Mariány'), ('SC', 'Seychely'), ('SL', 'Sierra Leone'), ('SG', 'Singapur'), ('SK', 'Slovenská republika'), ('SI', 'Slovinsko'), ('SO', 'Somálsko'), ('AE', 'Spojené arabské emiráty'), ('US', 'Spojené štáty, USA'), ('RS', 'Srbsko'), ('LK', 'Srí Lanka'), ('CF', 'Stredoafrická republika'), ('SD', 'Sudán'), ('SR', 'Surinam'), ('SZ', 'Svazijsko'), ('SH', 'Svätá Helena'), ('LC', 'Svätá Lucia'), ('KN', 'Svätý Krištof a Nevis'), ('SX', 'Svätý Martin'), ('ST', 'Svätý Tomáš a Princov ostrov'), ('VC', 'Svätý Vincent a Grenadíny'), ('SY', 'Sýria'), ('SB', 'Šalamúnove ostrovy'), ('ES', 'Španielsko'), ('CH', 'Švajčiarsko'), ('SE', 'Švédsko'), ('TJ', 'Tadžikistan'), ('TW', 'Taiwan'), ('IT', 'Taliansko'), ('TZ', 'Tanzánia'), ('TH', 'Thajsko'), ('TG', 'Togo'), ('TO', 'Tonga'), ('TT', 'Trinidad a Tobago'), ('TN', 'Tunisko'), ('TR', 'Turecko'), ('TM', 'Turkménsko'), ('TC', 'Turks a Caicos'), ('TV', 'Tuvalu'), ('UG', 'Uganda '), ('UA', 'Ukrajina'), ('UY', 'Uruguaj'), ('UZ', 'Uzbekistan'), ('VU', 'Vanuatu'), ('VA', 'Vatikán'), ('GB', 'Veľká Británia'), ('VE', 'Venezuela'), ('VN', 'Vietnam'), ('TL', 'Východný Timor'), ('ZM', 'Zambia'), ('EH', 'Západná Sahara'), ('ZW', 'Zimbabwe')], default='SK', max_length=30)),
                ('brewery_city', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('place', models.CharField(blank=True, max_length=70, null=True)),
                ('serving', models.BooleanField(choices=[(True, 'fľašové'), (False, 'čapované')], default=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('price', models.FloatField(blank=True, null=True)),
                ('volume', models.FloatField(choices=[(0.1, '0,1l'), (0.2, '0,2l'), (0.3, '0,3l'), (0.33, '0,33l'), (0.4, '0,4l'), (0.5, '0,5l'), (0.75, '0,75l'), (1, '1l')], default=0.5, max_length=10)),
                ('note', models.TextField(blank=True, null=True)),
                ('rating', models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=3)),
            ],
        ),
        migrations.RemoveField(
            model_name='beer',
            name='city',
        ),
        migrations.RemoveField(
            model_name='beer',
            name='country',
        ),
        migrations.RemoveField(
            model_name='beer',
            name='date',
        ),
        migrations.RemoveField(
            model_name='beer',
            name='note',
        ),
        migrations.RemoveField(
            model_name='beer',
            name='place',
        ),
        migrations.RemoveField(
            model_name='beer',
            name='price',
        ),
        migrations.RemoveField(
            model_name='beer',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='beer',
            name='serving',
        ),
        migrations.RemoveField(
            model_name='beer',
            name='volume',
        ),
        migrations.AlterField(
            model_name='beer',
            name='brewery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beers.Brewery'),
        ),
        migrations.AddField(
            model_name='rating',
            name='beer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beers.Beer'),
        ),
        migrations.AddField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
