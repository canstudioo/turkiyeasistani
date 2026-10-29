# Türkiye Asistanı yasal sayfaları — statik site üretici (GitHub Pages). Çalıştır: python build.py
# Kaynak metinler web/src/routes/{kosullar,gizlilik,destek}.tsx'ten alındı (2026-10-29), Gemini/Supabase'e göre güncellendi.
import html
import pathlib

CONTACT = "jokeriblanc@icloud.com"
UPDATED = "29 Ekim 2026"
HERE = pathlib.Path(__file__).parent

CSS = """
:root{--bg:#E7EEF9;--fg:#12192B;--muted:#576076;--card:rgba(255,255,255,.82);--primary:#4D77FC;--border:rgba(255,255,255,.9)}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;color:var(--fg);
background:var(--bg) radial-gradient(circle at 10% 0%,rgba(77,119,252,.25),transparent 45%) no-repeat;min-height:100vh}
main{max-width:720px;margin:0 auto;padding:40px 16px 56px}
.brand{display:flex;align-items:center;gap:12px;text-decoration:none;color:var(--fg);font-weight:800;font-size:18px}
.brand img{width:44px;height:44px;border-radius:12px}
h1{font-size:28px;margin:28px 0 6px}
.lead{color:var(--muted);margin:0 0 4px}
.card{background:var(--card);border:2px solid var(--border);border-radius:20px;padding:18px 20px;margin-top:12px;box-shadow:0 10px 24px rgba(77,119,252,.10)}
.card h2{font-size:16px;margin:0 0 6px}.card p{margin:0;color:var(--muted);font-size:14.5px;line-height:1.6}
.note{background:rgba(77,119,252,.10);border-radius:16px;padding:14px 16px;margin-top:14px;font-size:13.5px}
nav.links{display:flex;flex-wrap:wrap;gap:18px;justify-content:center;margin-top:28px;font-weight:700;font-size:14px}
a{color:var(--primary)}
"""


def page(slug, title, lead, cards, notes=()):
    root = "../" if slug else "./"
    body = "\n".join(f'<section class="card"><h2>{html.escape(t)}</h2><p>{b}</p></section>' for t, b in cards)
    note = "\n".join(f'<div class="note">{n}</div>' for n in notes)
    doc = f"""<!doctype html><html lang="tr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)} — Türkiye Asistanı</title>
<meta name="description" content="{html.escape(lead)}">
<link rel="icon" href="{root}icon.png"><style>{CSS}</style></head><body><main>
<a class="brand" href="{root}"><img src="{root}icon.png" alt="">Türkiye Asistanı</a>
<h1>{html.escape(title)}</h1><p class="lead">{html.escape(lead)}</p>
{body}
{note}
<nav class="links"><a href="{root}kosullar/">Kullanım Koşulları</a><a href="{root}gizlilik/">Gizlilik</a><a href="{root}destek/">Destek</a></nav>
</main></body></html>"""
    out = HERE / slug / "index.html" if slug else HERE / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(doc, encoding="utf-8")


MAIL = f'<a href="mailto:{CONTACT}">{CONTACT}</a>'
EULA = "https://www.apple.com/legal/internet-services/itunes/dev/stdeula/"

page("kosullar", "Kullanım Koşulları", "Sade bir dille: uygulamayı nasıl kullanabilirsin?", [
    ("Türkiye Asistanı nedir?", "İşlerini, hatırlatıcılarını ve belgelerini bir arada takip etmene yardım eden kişisel bir düzen asistanıdır. Türkiye Asistanı resmi bir devlet uygulaması değildir ve hiçbir kurumu temsil etmez."),
    ("Asistan'ın yanıtları", "Asistan yapay zekâ ile çalışır ve yanıtları bilgi amaçlıdır; hatalı ya da eksik olabilir. Resmi bir işlem yapmadan önce ilgili kurumun güncel bilgisini kontrol etmelisin. Asistan senin adına iş veya hatırlatıcı oluşturmadan önce onayını ister."),
    ("Hesabın ve sorumluluğun", "Hesabının güvenliği sana aittir. Yalnızca kendi bilgilerini ve belgelerini yükle. e-Devlet şifresi, banka şifresi veya kart bilgisi gibi giriş bilgilerini uygulamaya ya da Asistan'a yazma."),
    ("Planlar ve kullanım hakları", "Temel uygulama (İşlerim, Hatırlatıcılar, Takvim, Inbox ve temel belge işlemleri) Ücretsiz Plan'da kullanılabilir. Asistan'ın günlük kullanım hakkı plana göre değişir: Ücretsiz Plan'da günde 5, Premium'da günde 50 istek. Bu sayılar zamanla değişebilir."),
    ("Premium abonelik", "Premium abonelik aylık (149,99 TL) ya da yıllık (1.299,99 TL) seçenekleriyle sunulur. Satın alma yalnızca mobil uygulamada, App Store üzerinden yapılır; mağazada gösterilen fiyat esas alınır. Abonelik, dönem bitiminden en az 24 saat önce iptal edilmezse otomatik olarak yenilenir. İptal ettiğinde ödenmiş dönemin sonuna kadar Premium erişimin sürer. Aboneliğini ve iptalini mağaza hesap ayarlarından yönetebilirsin. Premium hesabına aittir; aynı hesapla girdiğin her yerde geçerlidir."),
    ("Apple Standart Lisans Sözleşmesi", f'App Store üzerinden indirilen uygulama için Apple\'ın Standart Son Kullanıcı Lisans Sözleşmesi (EULA) de geçerlidir: <a href="{EULA}">{EULA}</a>'),
    ("Hesabını silmek", "Hesabını istediğin zaman Profil &gt; Hesabı sil bölümünden kalıcı olarak silebilirsin. Bu işlem geri alınamaz; hesabın ve tüm verilerin silinir."),
    ("Değişiklikler", "Bu bilgileri zaman zaman güncelleyebiliriz. Güncel hâli her zaman bu sayfada yer alır."),
], ["Bu sayfa genel bilgilendirme amaçlıdır ve hukuki danışmanlık yerine geçmez."])

page("gizlilik", "Gizlilik", "Sade bir dille: verilerin bizde nasıl duruyor?", [
    ("1. Giriş ve Kapsam", "Bu Gizlilik Politikası, Türkiye Asistanı uygulamasını kullanırken hangi kişisel verilerin toplandığını, nasıl işlendiğini ve haklarının neler olduğunu açıklar. Uygulamayı kullanarak bu politikada açıklanan uygulamaları kabul etmiş olursun."),
    ("2. Topladığımız Bilgiler", "Adın, e-posta adresin, seçtiğin ilgi alanların, oluşturduğun işler ve hatırlatıcılar, yüklediğin belgeler, bildirim tercihlerin ve uygulamayı kullanırken oluşan temel kullanım verileri (ör. oturum açma zamanı) toplanır. Ödemeleri Apple işler; kart bilgilerin bize ulaşmaz."),
    ("3. Bilgilerini Neden İşliyoruz", "Verilerini yalnızca sana ait işleri hatırlatabilmek, belgelerini bir arada tutabilmek, ana sayfada senin için önemli olanı gösterebilmek, hesabını doğrulayabilmek ve uygulamayı iyileştirebilmek için işliyoruz. İşleme faaliyetlerimiz; sözleşmenin ifası, açık rızan ve meşru menfaatimiz hukuki sebeplerine dayanır."),
    ("4. Belgelerin Saklanması ve Korunması", "Yüklediğin belgeler şifreli bir alanda, erişim kontrolüyle korunarak saklanır. Belgelerin herkese açık bir bağlantısı yoktur; yalnızca sen giriş yaptığında, kısa süre geçerli imzalı bir bağlantıyla açılır. Başka kullanıcılar belgelerini hiçbir şekilde göremez."),
    ("5. Yapay Zekâ Asistanı ve Veri İşleme", "Asistana sorduğun soru, yanıt için gereken kayıtların (ör. iş ve hatırlatıcı başlıkları) ve analiz için seçtiğin belge, yanıt üretmek amacıyla Google'ın Gemini yapay zekâ hizmetine gönderilir. Bu içerikler Google'ın Gemini API şartlarına göre işlenir; Google bunları hizmetlerini geliştirmek için kullanabilir. Bu yüzden Asistan'a ve analiz edilecek belgelere gereksiz kişisel bilgi (ör. T.C. kimlik numarası, banka bilgisi) koyma. Asistan senin adına hiçbir şeyi kendi başına kaydetmez veya göndermez; iş ya da hatırlatıcı oluşturmadan önce açık onayını ister."),
    ("6. Üçüncü Taraflarla Paylaşım", "Verilerini; barındırma ve kimlik doğrulama (Supabase), yapay zekâ yanıtları (Google Gemini) ve ödeme işleme (Apple) hizmetlerini sağlayan altyapı sağlayıcılarımız dışında hiçbir üçüncü tarafla paylaşmıyoruz, satmıyoruz veya reklam amaçlı kullanmıyoruz. Yasal bir zorunluluk olması hâlinde yetkili mercilerle paylaşım yapılabilir."),
    ("7. Veri Saklama Süresi", "Verilerini, hesabın aktif olduğu sürece ve hizmeti sana sunabilmek için gereken süre boyunca saklarız. Hesabını sildiğinde ilişkili tüm veriler, yasal saklama yükümlülüğü bulunmadığı sürece kalıcı olarak ve geri alınamaz şekilde silinir."),
    ("8. Veri Güvenliği", "Verilerin şifreleme ve erişim kontrolüyle korunur. e-Devlet şifresi, banka şifresi, kart bilgisi veya benzeri hassas giriş bilgilerini asla istemiyoruz ve saklamıyoruz; bu tür bilgileri uygulamaya hiçbir şekilde girme."),
    ("9. Hakların", "6698 sayılı Kişisel Verilerin Korunması Kanunu (KVKK) ve ilgili mevzuat kapsamında; verilerinin işlenip işlenmediğini öğrenme, işlenmişse buna ilişkin bilgi talep etme, düzeltilmesini veya silinmesini isteme ve işlemeye itiraz etme hakkına sahipsin. Bu haklarını kullanmak için bize aşağıdaki iletişim kanalından ulaşabilirsin."),
    ("10. Çocukların Gizliliği", "Türkiye Asistanı 13 yaşın altındaki kullanıcılara yönelik değildir ve bu yaş grubundan bilerek veri toplamayız. 13 yaşın altında bir çocuğun bize veri sağladığını öğrenirsek, bu verileri derhal sileriz."),
    ("11. Hesap ve Veri Silme", "İşlerini ve belgelerini uygulama içinden istediğin an tek tek silebilirsin. Hesabının tamamen silinmesini istersen Profil &gt; Hesabı sil bölümünden hesabını kalıcı olarak silebilirsin. Uygulamaya erişemiyorsan aynı talebi aşağıdaki e-posta adresinden de iletebilirsin."),
    ("12. Politika Değişiklikleri ve İletişim", f"Bu politikada değişiklik yaparsak, güncel sürümü bu sayfada yayımlarız. Gizlilikle ilgili sorularını {MAIL} adresine yazarak bize iletebilirsin."),
], [f"Son güncelleme: {UPDATED}", "Uygulamadaki resmi işlem rehberleri bilgi amaçlıdır. Resmi işlem öncesinde ilgili kurumun güncel bilgisini kontrol et."])

page("destek", "Destek", "Bir sorun mu var? Önce aşağıdaki cevaplara bak, çözülmezse bize yaz.", [
    ("Bize ulaş", f"Sorularını, önerilerini ve sorunlarını {MAIL} adresine yazabilirsin. Mesajında hangi hesapla giriş yaptığını ve ne olduğunu kısaca anlatman çözümü hızlandırır."),
    ("Premium aboneliğimi nasıl yönetir ya da iptal ederim?", "Profil sayfasındaki “Aboneliği yönet” düğmesine bas; Apple Kimliğinin abonelik ayarları açılır. iPhone'da aynı yere Ayarlar &gt; adın &gt; Abonelikler yolundan da ulaşabilirsin. İptal ettiğinde, ödediğin dönemin sonuna kadar Premium erişimin devam eder."),
    ("Satın aldığım Premium görünmüyor, ne yapmalıyım?", "Aynı hesapla giriş yaptığından emin ol. Sonra Profil &gt; Premium sayfasında “Satın alımları geri yükle” düğmesine bas."),
    ("Şifremi unuttum.", f"Giriş ekranındaki “Şifremi unuttum” bağlantısını kullan. E-posta gelmezse {MAIL} adresine yaz, hesabına yeniden erişmene yardım edelim."),
    ("Verilerimi nasıl silerim?", "Profil &gt; Hesabı sil bölümünden hesabını ve tüm verilerini kalıcı olarak silebilirsin. Verilerinin nasıl saklandığını Gizlilik sayfasında açıkladık."),
], ["Türkiye Asistanı resmi bir devlet uygulaması değildir. e-Devlet, banka veya kart şifreni asla istemez."])

page("", "Türkiye Asistanı", "Ne yapman gerektiğini söyle, gerisini senin için takip edelim.", [
    ("Uygulama", 'İşlerini, hatırlatıcılarını, belgelerini ve son tarihlerini tek yerde tut; yapay zekâ asistanı resmi yazıları sade dille anlatsın. <a href="https://apps.apple.com/tr/app/id6814012417">App Store\'da ücretsiz indir</a>.'),
])
print("ok")
