# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-19 19:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0018_auto_20171019_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brewery',
            name='country',
            field=models.CharField(choices=[('', 'Vyberte krajinu'), ('AF', 'Afganistan'), ('AL', 'Albánsko'), ('DZ', 'Alžírsko'), ('AD', 'Andorra'), ('AO', 'Angola'), ('AI', 'Anguilla'), ('AG', 'Antigua a Barbuda'), ('AR', 'Argentína'), ('AM', 'Arménsko'), ('AW', 'Aruba'), ('AU', 'Austrália'), ('AZ', 'Azerbajdžan'), ('BS', 'Bahamy'), ('BH', 'Bahrajn'), ('BD', 'Bangladéš'), ('BB', 'Barbados'), ('BE', 'Belgicko'), ('BZ', 'Belize'), ('BJ', 'Benin'), ('BM', 'Bermudy'), ('BT', 'Bhután'), ('BY', 'Bielorusko'), ('BO', 'Bolívia'), ('BQ', 'Bonaire, Svätý Eustach a Saba'), ('BA', 'Bosna a Hercegovina'), ('BW', 'Botswana'), ('BV', 'Bouvetov ostrov'), ('BR', 'Brazília'), ('VG', 'Britské Panenské ostrovy'), ('BN', 'Brunej'), ('BG', 'Bulharsko'), ('BF', 'Burkina'), ('BI', 'Burundi'), ('CK', 'Cookove ostrovy'), ('CW', 'Curacao'), ('CY', 'Cyprus'), ('TD', 'Čad'), ('CZ', 'Česká republika'), ('ME', 'Čierna Hora'), ('CL', 'Čile'), ('CN', 'Čína'), ('DK', 'Dánsko'), ('DM', 'Dominika'), ('DO', 'Dominikánska republika'), ('DJ', 'Džibutsko'), ('EG', 'Egypt'), ('EC', 'Ekvádor'), ('ER', 'Eritrea'), ('EE', 'Estónsko'), ('ET', 'Etiópia'), ('FO', 'Faerské ostrovy'), ('FK', 'Falklandy'), ('FJ', 'Fidži'), ('PH', 'Filipíny'), ('FI', 'Fínsko'), ('FR', 'Francúzsko'), ('GA', 'Gabon'), ('GM', 'Gambia'), ('GH', 'Ghana'), ('GI', 'Gibraltár'), ('GR', 'Grécko'), ('GD', 'Grenada'), ('GL', 'Grónsko'), ('GE', 'Gruzínsko'), ('GT', 'Guatemala'), ('GG', 'Guernsey'), ('GN', 'Guinea'), ('GW', 'Guinea-Bissau'), ('GY', 'Guyana'), ('HT', 'Haiti'), ('NL', 'Holandsko'), ('HN', 'Honduras'), ('HK', 'Hongkong'), ('HR', 'Chorvátsko'), ('IN', 'India'), ('ID', 'Indonézia'), ('XX', 'Iné'), ('IQ', 'Irak'), ('IR', 'Irán'), ('IS', 'Island'), ('IL', 'Izrael'), ('IE', 'Írsko'), ('JM', 'Jamajka'), ('JP', 'Japonsko'), ('YE', 'Jemen'), ('JE', 'Jersey'), ('JO', 'Jordánsko'), ('ZA', 'Južná Afrika'), ('GS', 'Južná Georgia a Južné Sandwichove ostrovy'), ('SS', 'Južný Sudán'), ('KY', 'Kajmanie ostrovy'), ('KH', 'Kambodža'), ('CM', 'Kamerun'), ('CA', 'Kanada'), ('CV', 'Kapverdy'), ('QA', 'Katar'), ('KZ', 'Kazachstan'), ('KE', 'Keňa'), ('KG', 'Kirgizsko'), ('KI', 'Kiribati'), ('CO', 'Kolumbia'), ('KM', 'Komory'), ('CD', 'Kongo (býv. Zair)'), ('CG', 'Kongo'), ('KR', 'Kórejská republika'), ('KP', 'Kórejská ľudovodemokratická republika (KĽDR)'), ('CR', 'Kostarika'), ('CU', 'Kuba'), ('KW', 'Kuvajt'), ('LA', 'Laos'), ('LS', 'Lesotho'), ('LB', 'Libanon'), ('LR', 'Libéria'), ('LY', 'Líbya'), ('LI', 'Lichtenštajnsko'), ('LT', 'Litva'), ('LV', 'Lotyšsko'), ('LU', 'Luxembursko'), ('MO', 'Macao'), ('MK', 'Macedónsko'), ('MG', 'Madagaskar'), ('MY', 'Malajzia'), ('MW', 'Malawi'), ('MV', 'Maldivy'), ('ML', 'Mali'), ('MT', 'Malta'), ('IM', 'Man'), ('MA', 'Maroko'), ('MU', 'Maurícius'), ('MR', 'Mauritánia'), ('HU', 'Maďarsko'), ('MX', 'Mexiko'), ('MM', 'Mjanmarsko'), ('MD', 'Moldavsko'), ('MC', 'Monako'), ('MN', 'Mongolsko'), ('MS', 'Montserrat'), ('MZ', 'Mozambik'), ('NA', 'Namíbia'), ('NR', 'Nauru'), ('DE', 'Nemecko'), ('NP', 'Nepál'), ('NE', 'Niger'), ('NG', 'Nigéria'), ('NI', 'Nikaragua'), ('NO', 'Nórsko'), ('NZ', 'Nový Zéland'), ('OM', 'Omán '), ('PK', 'Pakistan'), ('PW', 'Palau'), ('PA', 'Panama'), ('PG', 'Papua-Nová Guinea'), ('PY', 'Paraguaj'), ('PE', 'Peru'), ('CI', 'Pobrežie Slonoviny'), ('PL', 'Poľsko'), ('PT', 'Portugalsko'), ('AT', 'Rakúsko'), ('GQ', 'Rovníková Guinea'), ('RO', 'Rumunsko'), ('RU', 'Ruská federácia'), ('RW', 'Rwanda'), ('SV', 'Salvádor'), ('WS', 'Samoa'), ('SM', 'San Maríno'), ('SA', 'Saudská Arábia'), ('SN', 'Senegal'), ('MP', 'Severné Mariány'), ('SC', 'Seychely'), ('SL', 'Sierra Leone'), ('SG', 'Singapur'), ('SK', 'Slovenská republika'), ('SI', 'Slovinsko'), ('SO', 'Somálsko'), ('AE', 'Spojené arabské emiráty'), ('US', 'Spojené štáty, USA'), ('RS', 'Srbsko'), ('LK', 'Srí Lanka'), ('CF', 'Stredoafrická republika'), ('SD', 'Sudán'), ('SR', 'Surinam'), ('SZ', 'Svazijsko'), ('SH', 'Svätá Helena'), ('LC', 'Svätá Lucia'), ('KN', 'Svätý Krištof a Nevis'), ('SX', 'Svätý Martin'), ('ST', 'Svätý Tomáš a Princov ostrov'), ('VC', 'Svätý Vincent a Grenadíny'), ('SY', 'Sýria'), ('SB', 'Šalamúnove ostrovy'), ('ES', 'Španielsko'), ('CH', 'Švajčiarsko'), ('SE', 'Švédsko'), ('TJ', 'Tadžikistan'), ('TW', 'Taiwan'), ('IT', 'Taliansko'), ('TZ', 'Tanzánia'), ('TH', 'Thajsko'), ('TG', 'Togo'), ('TO', 'Tonga'), ('TT', 'Trinidad a Tobago'), ('TN', 'Tunisko'), ('TR', 'Turecko'), ('TM', 'Turkménsko'), ('TC', 'Turks a Caicos'), ('TV', 'Tuvalu'), ('UG', 'Uganda '), ('UA', 'Ukrajina'), ('UY', 'Uruguaj'), ('UZ', 'Uzbekistan'), ('VU', 'Vanuatu'), ('VA', 'Vatikán'), ('GB', 'Veľká Británia'), ('VE', 'Venezuela'), ('VN', 'Vietnam'), ('TL', 'Východný Timor'), ('ZM', 'Zambia'), ('EH', 'Západná Sahara'), ('ZW', 'Zimbabwe')], max_length=30),
        ),
    ]
