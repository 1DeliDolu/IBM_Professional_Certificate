

## A) Önerilen Akış: Tek Uygulama (create + update)

```bash
# 0) Code Engine’de aktif projeyi kontrol et
ibmcloud ce project current

# 1) Kodu indir / klasöre gir
cd /home/project
[ -d fyidw-guess-the-capital ] || git clone https://github.com/ibm-developer-skills-network/fyidw-guess-the-capital.git
cd fyidw-guess-the-capital

# 2) (Opsiyonel) Yerelde Docker ile hızlı test
docker build -t guess-the-capital:local .
docker run --rm -d -p 8080:80 --name guess-the-capital-local guess-the-capital:local
# Tarayıcıdan/preview ile test et (host:8080)
docker stop guess-the-capital-local

# 3) ICR’ye (IBM Container Registry) build + push
# Not: "latest" üzerine yazmak yerine ayrıca benzersiz tag basmak iyi pratiktir.
TAG=$(date +%Y%m%d%H%M%S)
IMAGE=us.icr.io/${SN_ICR_NAMESPACE}/guess-the-capital:${TAG}
LATEST=us.icr.io/${SN_ICR_NAMESPACE}/guess-the-capital:latest

ibmcloud cr login
docker build -t "$IMAGE" -t "$LATEST" .
docker push "$IMAGE"
docker push "$LATEST"

# 4) Code Engine’e deploy (varsa update, yoksa create)
APP=guess-the-capital

if ibmcloud ce application get --name "$APP" >/dev/null 2>&1; then
  ibmcloud ce application update --name "$APP" --image "$IMAGE" --registry-secret icr-secret --port 80
else
  ibmcloud ce application create --name "$APP" --image "$IMAGE" --registry-secret icr-secret --port 80
fi

# 5) Durumu ve URL’yi gör
ibmcloud ce application get --name "$APP"
ibmcloud ce application list
```

**Neden bu daha iyi?**

* Aynı app’i “delete + create” ile yeniden kurmak yerine **update** ile daha temiz ve genelde daha az kesintili ilerlersin.
* `TAG` ile **immutability** sağlarsın (hangi sürümü deploy ettiğin net olur).

---

## B) Alternatif: v2 ile Blue/Green (Paralel Yayın)

```bash
# Varsayım: IMAGE already pushed (A bölümündeki 3. adım)

# Eski uygulama çalışırken v2’yi oluştur
ibmcloud ce application create \
  --name guess-the-capital-v2 \
  --image us.icr.io/${SN_ICR_NAMESPACE}/guess-the-capital:latest \
  --registry-secret icr-secret \
  --port 80

# v2’yi kontrol et (URL al, test et)
ibmcloud ce application get --name guess-the-capital-v2

# Her şey tamam ise eskiyi sil (cutover yaklaşımı)
ibmcloud ce application delete --name guess-the-capital

# İstersen v2’yi ana isimle yeniden oluştur (veya v2 ismini koru)
ibmcloud ce application create \
  --name guess-the-capital \
  --image us.icr.io/${SN_ICR_NAMESPACE}/guess-the-capital:latest \
  --registry-secret icr-secret \
  --port 80

# Listele
ibmcloud ce application list
```

---

İstersen senin çıktına göre (ör. `icr-secret` yoksa) **secret oluşturma** adımını da aynı akışa ekleyeyim.
