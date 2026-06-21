<section aria-labelledby="visual-learning-preservation-heading" class="card-surface appendix visual-preservation-note" id="visual-learning-preservation-note">
  <h2 id="visual-learning-preservation-heading">یادداشت حفظ یادگیری دیداری</h2>

  <h3>هدف این یادداشت</h3>
  <p>این یادداشت برای انتقال روح آموزشی TUYA به کل جزوه اضافه شده است، اما جایگزین بخش‌های مفهومی نیست. بخش مفهومی باید حفظ شود و هرجا لازم است دقیق‌تر، ساده‌تر و مستندتر شود. تغییر اصلی باید در تمرین‌ها اتفاق بیفتد: تمرین نباید فقط بگوید «این مقدار را تنظیم کن»؛ باید مسیر فکر طراح را شبیه‌سازی کند.</p>

  <h3>اصل مادر: هر تغییر در Context انجام می‌شود</h3>
  <p>قبل از هر تغییر در Elementor باید Context روشن باشد: کدام Element انتخاب شده، کدام Class فعال است، کدام Breakpoint دیده می‌شود، کدام State در حال ویرایش است و تغییر قرار است Local باشد یا Global. اگر استایلی دیده نمی‌شود، اولین اقدام حفظی یا حدسی نیست؛ بررسی Context است.</p>
  <p>این اصل باید به‌عنوان نخ اتصال درس‌ها حفظ شود: ابتدا Tree و Parent/Child، بعد Display و Flow، بعد اندازه و واحد، بعد Position و Layering، سپس Responsive، Design System، DOM و Audit.</p>

  <h3>تفاوت نقش بخش مفهومی و بخش تمرین</h3>
  <ul>
    <li><strong>بخش مفهومی:</strong> باید تعریف، تشبیه، مثال ذهنی، دام‌های رایج، قوانین طلایی و جدول‌های مقایسه‌ای را نگه دارد و کامل‌تر کند.</li>
    <li><strong>بخش تمرین:</strong> باید مربی مرحله‌به‌مرحله باشد: وضعیت را بخواند، شواهد را جدا کند، فقط یک اقدام کوچک بدهد و بعد منتظر تأیید بماند.</li>
    <li><strong>بخش اصلاحی:</strong> هرجا جزوه با رابط واقعی Elementor V4، اسکرین‌شات کاربر یا مستندات رسمی مغایرت داشت، مغایرت باید آشکارا ثبت شود؛ مقدار پیشنهادی نباید حکم قطعی جزوه معرفی شود.</li>
  </ul>

  <h3>قالب الزامی برای تمرین‌ها</h3>
  <p>تمرین‌های عملی، مخصوصاً تمرین‌های TUYA، باید با این الگو بازنویسی شوند:</p>
  <ol>
    <li><strong>وضعیت تأییدشده:</strong> چه چیزی از اسکرین‌شات یا گزارش کاربر confirmed است؟</li>
    <li><strong>وضعیت نامطمئن:</strong> چه چیزی provisional یا unknown است و نباید قطعی فرض شود؟</li>
    <li><strong>نسبت با جزوه:</strong> آیا اقدام همسو با جزوه است، در جزوه صریح نیست، یا جزوه نیاز به اصلاح دارد؟</li>
    <li><strong>یک اقدام کوچک:</strong> مسیر UI، Element هدف، Class فعال، Property، مقدار و واحد باید جداگانه نوشته شود.</li>
    <li><strong>مرز اثر:</strong> مشخص شود تغییر Local است یا Global و روی چه عناصر دیگری اثر می‌گذارد.</li>
    <li><strong>تأیید پایانی:</strong> کاربر باید دقیقاً بداند بعد از انجام کار چه چیزی را گزارش یا اسکرین‌شات کند.</li>
  </ol>

  <h3>زنجیرهٔ مفهومی که باید در کل جزوه حفظ شود</h3>
  <p>جزوه نباید مجموعه‌ای از مفاهیم جدا باشد. مسیر درست یادگیری چنین است:</p>
  <ol>
    <li><strong>Context:</strong> اول بدانیم در کدام Element، Class، State و Breakpoint هستیم.</li>
    <li><strong>Structure:</strong> بعد Tree، Parent، Child و مسئولیت هر ظرف را مشخص کنیم.</li>
    <li><strong>Flow و Display:</strong> سپس بفهمیم Flow بستر چیدمان است و Display دستور رفتار Element و فرزندانش.</li>
    <li><strong>Size و Units:</strong> بعد Width، Percent، PX، VW، REM، Gap، Min و Max را نسبت به Parent یا Viewport بسنجیم.</li>
    <li><strong>Position و Layering:</strong> فقط وقتی Structure سالم است سراغ Relative، Absolute، Z-index و Overflow برویم.</li>
    <li><strong>Responsive:</strong> مقدارها را در Breakpointها وارث‌مند و قابل‌ردیابی کنترل کنیم.</li>
    <li><strong>Design System:</strong> مقدار مشترک در Variable، ظاهر مشترک در Global Class، تغییر اختصاصی در Local Class و ساختار تکرارشونده در Component قرار بگیرد.</li>
    <li><strong>DOM و Audit:</strong> در پایان بفهمیم خروجی Elementor فقط درخت بصری نیست؛ مرورگر DOM و Render Tree را می‌سازد و وزن ساختاری باید بررسی شود.</li>
  </ol>

  <h3>اصلاحات محتوایی که باید در درس‌ها پخش شوند</h3>
  <ul>
    <li><strong>Flow و Display یکی نیستند:</strong> Flow بستر رفتار طبیعی صفحه است؛ Display ویژگی‌ای است که رفتار خود Element و قوانین داخلی فرزندانش را تعیین می‌کند.</li>
    <li><strong>Absolute ابزار چیدمان اصلی نیست:</strong> ساختار اصلی باید در Normal Flow بماند. Absolute فقط برای Badge، تزئین کنترل‌شده، Nodeهای داخل Stage یا مواردی با مرجع روشن استفاده شود.</li>
    <li><strong>Percent همیشه وابسته به Parent است:</strong> مقدار درصدی را نباید مثل عدد مستقل خواند. قبل از مقداردهی باید والد بلافاصله و فضای محتوایی آن مشخص شود.</li>
    <li><strong>Min Height مقاوم‌تر از Height ثابت است:</strong> برای بخش‌هایی با محتوای پویا، min-height معمولاً امن‌تر از height ثابت است؛ height ثابت فقط بعد از بررسی واقعی محتوا و Breakpointها استفاده شود.</li>
    <li><strong>Rename در Structure:</strong> تغییر نام Element از منوی راست‌کلیک انجام نمی‌شود؛ روی نام Element در Structure دوبار کلیک شود.</li>
    <li><strong>DOM با درخت بصری یکی نیست:</strong> Structure یا درخت Elementor نمای ساده‌شدهٔ بصری است، اما DOM واقعی شامل Nodeهای نامرئی، Text Nodeها، head، script، style و وضعیت‌های اجرایی مرورگر هم هست.</li>
    <li><strong>Class و Component جنس متفاوت دارند:</strong> Variable مقدار نگه می‌دارد، Class روی Element موجود اعمال می‌شود، اما Component ساختار تکرارشونده را می‌سازد یا بازاستفاده‌پذیر می‌کند.</li>
  </ul>

  <h3>سیاست صحت و مستندات</h3>
  <p>هر گزارهٔ اجرایی باید سطح اطمینان داشته باشد. اگر چیزی از اسکرین‌شات یا گزارش کاربر دیده شده است confirmed است. اگر فقط از جزوه آمده، workbook_specified است. اگر در مستند رسمی به‌روز Elementor آمده، official_v4_documented است. اگر مقدار برای تطبیق بصری پیشنهاد شده، provisional_visual_tuning است. اگر شاهد کافی نداریم، unknown است.</p>
  <p>بنابراین مقدارهایی مثل مختصات Node، Shadow، Width، Gap یا Content Width نباید قطعی معرفی شوند مگر اینکه با رابط واقعی، Breakpoint مشخص و شاهد تصویری تأیید شده باشند.</p>

  <h3>قاعدهٔ بازنویسی بعدی</h3>
  <p>در نسخهٔ بعدی، این یادداشت باید به متن درس‌ها تزریق شود؛ نه اینکه فقط به‌عنوان ضمیمه باقی بماند. اولویت ادغام: درس 1 برای Context، درس 4 برای Width و Min Height، درس 5 تا 7 برای Display و Flow، درس 12 برای Position، درس 14 برای Responsive، درس 17 و تکمیلی‌های 18A تا 18C برای Design System، و درس 20 برای DOM و Audit.</p>
</section>
