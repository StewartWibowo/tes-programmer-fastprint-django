from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Produk
from .forms import ProdukForm

def produk_list(request):
    # Hanya menampilkan yang bisa dijual
    data_produk = Produk.objects.filter(status__nama_status='bisa dijual')
    return render(request, 'produk/index.html', {'produk_list': data_produk})

def produk_hapus(request, id):
    produk = get_object_or_404(Produk, id_produk=id)
    produk.delete()
    messages.success(request, "Produk berhasil dihapus!")
    return redirect('produk_list')

def produk_tambah(request):
    if request.method == 'POST':
        form = ProdukForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Produk berhasil ditambahkan!") 
            return redirect('produk_list')
        else:
            messages.error(request, "Gagal menambah produk. Periksa kembali inputan Anda.") 
    else:
        form = ProdukForm()
    return render(request, 'produk/form_produk.html', {'form': form, 'title': 'Tambah Produk'})

def produk_edit(request, id):
    produk = get_object_or_404(Produk, id_produk=id)
    if request.method == 'POST':
        form = ProdukForm(request.POST, instance=produk)
        if form.is_valid():
            form.save()
            messages.success(request, "Produk berhasil diperbarui!")
            return redirect('produk_list')
        else:
            messages.error(request, "Gagal memperbarui produk.") 
    else:
        form = ProdukForm(instance=produk)
    return render(request, 'produk/form_produk.html', {'form': form, 'title': 'Edit Produk'})