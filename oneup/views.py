from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Outsourcing, Manufacture, As, Logistics
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.utils import timezone
from .forms import AsForm
from django.core.paginator import Paginator
from django.db.models import Q
from oneup.resources import OutResource, ManResource, LogResource, AsResource

@login_required(login_url='common:login')
@permission_required('oneup.view_outsourcing', login_url='oneup:deny', raise_exception=False)
def index(request):
    """
       out 목록 출력
       """
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    so = request.GET.get('so', 'recent')  # 정렬기준

    # 정렬
    if so == 'code':
        outsourcing_list = Outsourcing.objects.order_by('ossn', '-osdate')
    elif so == 'que':
        outsourcing_list = Outsourcing.objects.order_by('-osqu', '-osdate')
    else:  # recent
        outsourcing_list = Outsourcing.objects.order_by('-osdate')

        # 조회
    if kw:
        outsourcing_list = outsourcing_list.filter(
            Q(ossn__icontains=kw) |  # 부품코드 검색
            Q(osqu__icontains=kw) |  # 납품수량 검색
            Q(osdate__icontains=kw)  # 납품일시 검색
        ).distinct()

        # 페이징처리
    paginator = Paginator(outsourcing_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'outsourcing_list': page_obj, 'page': page, 'kw': kw, 'so': so}  # page, kw, so가 추가되었다.
    return render(request, 'oneup/outsourcing_list.html', context)

@login_required(login_url='common:login')
@permission_required('oneup.view_manufacture', login_url='oneup:deny', raise_exception=False)
def manufacturer(request):
    """
       manu 목록 출력
       """
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    so = request.GET.get('so', 'recent')  # 정렬기준

    # 정렬
    if so == 'pro':
        manufacture_list = Manufacture.objects.order_by('-proname', '-mfdate')
    elif so == 'mfsn':
        manufacture_list = Manufacture.objects.order_by('-mfsn', '-mfdate')
    elif so == 'ori':
        manufacture_list = Manufacture.objects.order_by('-origin', '-mfdate')
    elif so == 'half':
        manufacture_list = Manufacture.objects.order_by('-halfpro', '-mfdate')
    elif so == 'work':
        manufacture_list = Manufacture.objects.order_by('-workercode', '-mfdate')
    elif so == 'mfst':
        manufacture_list = Manufacture.objects.order_by('-mfsta', '-mfdate')
    else:  # recent
        manufacture_list = Manufacture.objects.order_by('-mfdate')

        # 조회
    if kw:
        manufacture_list = manufacture_list.filter(
            Q(proname__icontains=kw) |  # 제품명 검색
            Q(mfsn__icontains=kw) |  # 시리얼넘버 검색
            Q(origin__icontains=kw) |  # 원자재 검색
            Q(halfpro__icontains=kw) |  # 반제품 검색
            Q(workercode__icontains=kw) |  # 작업자코드 검색
            Q(mfsta__icontains=kw) |  # 제작상태 검색
            Q(mfdate__icontains=kw)  # 업데이트 일시 검색
        ).distinct()

    # 페이징처리
    paginator = Paginator(manufacture_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'manufacture_list': page_obj, 'page': page, 'kw': kw, 'so': so}  # page, kw, so가 추가되었다.
    return render(request, 'oneup/manufacture_list.html', context)

@login_required(login_url='common:login')
@permission_required('oneup.view_logistics', login_url='oneup:deny', raise_exception=False)
def logistics(request):
    """
       log 목록 출력
       """
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    so = request.GET.get('so', 'logn')  # 정렬기준

    # 정렬
    if so == 'logcu':
        logistics_list = Logistics.objects.order_by('-logcustom')
    elif so == 'logsn':
        logistics_list = Logistics.objects.order_by('-logsn')
    elif so == 'wh':
        logistics_list = Logistics.objects.order_by('-wh')
    elif so == 'dis':
        logistics_list = Logistics.objects.order_by('-dis')
    elif so == 'agen':
        logistics_list = Logistics.objects.order_by('-agen')
    else: # logn
        logistics_list = Logistics.objects.order_by('-logname')

        # 조회
    if kw:
        logistics_list = logistics_list.filter(
            Q(logcustom__icontains=kw) |  # 고객 검색
            Q(logsn__icontains=kw) |  # 시리얼넘버 검색
            Q(wh__icontains=kw) |  # 보관창고 검색
            Q(dis__icontains=kw) |  # 총판 검색
            Q(agen__icontains=kw) |  # 대리점 검색
            Q(logname__icontains=kw)  # 제품명 검색
        ).distinct()

    # 페이징처리
    paginator = Paginator(logistics_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'logistics_list': page_obj, 'page': page, 'kw': kw, 'so': so}  # page, kw, so가 추가되었다.
    return render(request, 'oneup/logistics_list.html', context)

@login_required(login_url='common:login')
@permission_required('oneup.view_as', login_url='oneup:deny', raise_exception=False)
def after(request):
    """
       as 목록 출력
       """
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    so = request.GET.get('so', 'recent')  # 정렬기준

    # 정렬
    if so == 'asname':
        as_list = As.objects.order_by('asname', '-asdate')
    elif so == 'pronu':
        as_list = As.objects.order_by('pronumber', '-asdate')
    elif so == 'assta':
        as_list = As.objects.order_by('assta', '-asdate')
    else: # recent
        as_list = As.objects.order_by('-asdate')

        # 조회
    if kw:
        as_list = as_list.filter(
            Q(asname__icontains=kw) |  # 고객명 검색
            Q(ph__icontains=kw) |  # 전화번호 검색
            Q(pronumber__icontains=kw) |  # 제품번호 검색
            Q(assta__icontains=kw) |  # A/S현황 검색
            Q(record__icontains=kw) |  # 통화녹음 검색
            Q(asdate__icontains=kw)  # 등록일시 검색
        ).distinct()

    # 페이징처리
    paginator = Paginator(as_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'as_list': page_obj, 'page': page, 'kw': kw, 'so': so}  # page, kw, so가 추가되었다.
    return render(request, 'oneup/as_list.html', context)

@login_required(login_url='common:login')
def main(request):
    """
        메인 페이지 : 이동할 DB 선택
           """
    return render(request, 'oneup/main.html')

def deny(request):
    """
        권한없음
                   """
    return render(request, 'oneup/deny.html')

def as_create(request):
    """
    as 정보입력
    """
    if request.method == 'POST':
        form = AsForm(request.POST)
        if form.is_valid():
            As = form.save(commit=False)
            As.asdate = timezone.now()
            As.save()
            messages.success(request, '제출해 주셔서 감사합니다!')
            return redirect('oneup:as_create')
    else:
        form = AsForm()
    context = {'form': form}
    return render(request, 'oneup/as_form.html', context)

def export1(request):
    out_resource = OutResource()
    dataset = out_resource.export()
    response = HttpResponse(dataset.xls, content_type='text/xls')
    response['Content-Disposition'] = 'attachment; filename="outsourcing.xls"'
    return response

def export2(request):
    man_resource = ManResource()
    dataset = man_resource.export()
    response = HttpResponse(dataset.xls, content_type='text/xls')
    response['Content-Disposition'] = 'attachment; filename="manufacture.xls"'
    return response

def export3(request):
    log_resource = LogResource()
    dataset = log_resource.export()
    response = HttpResponse(dataset.xls, content_type='text/xls')
    response['Content-Disposition'] = 'attachment; filename="logistics.xls"'
    return response

def export4(request):
    as_resource = AsResource()
    dataset = as_resource.export()
    response = HttpResponse(dataset.xls, content_type='text/xls')
    response['Content-Disposition'] = 'attachment; filename="AS.xls"'
    return response