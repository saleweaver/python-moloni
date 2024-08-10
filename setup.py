from setuptools import setup

from moloni.__version__ import __version__

setup(
    name='python-moloni',
    version=__version__,
    install_requires=[
        "requests",
        "cachetools>=4.2",
        "pydantic"
    ],
    extras_require={
        "aws-caching": ["aws-secretsmanager-caching", "boto3"],
        "aws": ["boto3"]
    },
    packages=['moloni.api', 'moloni.base', 'moloni.api.BankaccountsClient', 'moloni.api.BankaccountsCountModifiedSinceModel', 'moloni.api.BankaccountsDeleteModel', 'moloni.api.BankaccountsGetAllModel', 'moloni.api.BankaccountsInsertModel', 'moloni.api.BankaccountsUpdateModel', 'moloni.api.BillsofladingClient', 'moloni.api.BillsofladingCountModel', 'moloni.api.BillsofladingDeleteModel', 'moloni.api.BillsofladingGetAllModel', 'moloni.api.BillsofladingGetOneModel', 'moloni.api.BillsofladingInsertModel', 'moloni.api.BillsofladingSetTransportCodeModel', 'moloni.api.BillsofladingUpdateModel', 'moloni.api.CompaniesClient', 'moloni.api.CompaniesGetOneModel', 'moloni.api.CompaniesUpdateModel', 'moloni.api.CountriesClient', 'moloni.api.CountriesCountModifiedSinceModel', 'moloni.api.CountriesGetModifiedSinceModel', 'moloni.api.CreditnotesClient', 'moloni.api.CreditnotesCountModel', 'moloni.api.CreditnotesDeleteModel', 'moloni.api.CreditnotesGetAllModel', 'moloni.api.CreditnotesGetOneModel', 'moloni.api.CreditnotesInsertModel', 'moloni.api.CreditnotesUpdateModel', 'moloni.api.CurrenciesClient', 'moloni.api.CurrenciesCountModifiedSinceModel', 'moloni.api.CurrenciesGetModifiedSinceModel', 'moloni.api.CustomeralternateaddressesClient', 'moloni.api.CustomeralternateaddressesCountModifiedSinceModel', 'moloni.api.CustomeralternateaddressesDeleteModel', 'moloni.api.CustomeralternateaddressesGetAllModel', 'moloni.api.CustomeralternateaddressesGetModifiedSinceModel', 'moloni.api.CustomeralternateaddressesInsertModel', 'moloni.api.CustomeralternateaddressesUpdateModel', 'moloni.api.CustomerreturnnotesClient', 'moloni.api.CustomerreturnnotesCountModel', 'moloni.api.CustomerreturnnotesDeleteModel', 'moloni.api.CustomerreturnnotesGetAllModel', 'moloni.api.CustomerreturnnotesGetOneModel', 'moloni.api.CustomerreturnnotesInsertModel', 'moloni.api.CustomerreturnnotesSetTransportCodeModel', 'moloni.api.CustomerreturnnotesUpdateModel', 'moloni.api.CustomersClient', 'moloni.api.CustomersCountByNameModel', 'moloni.api.CustomersCountByNumberModel', 'moloni.api.CustomersCountBySearchModel', 'moloni.api.CustomersCountByVatModel', 'moloni.api.CustomersCountModel', 'moloni.api.CustomersCountModifiedSinceModel', 'moloni.api.CustomersDeleteModel', 'moloni.api.CustomersGetAllModel', 'moloni.api.CustomersGetByNameModel', 'moloni.api.CustomersGetByNumberModel', 'moloni.api.CustomersGetBySearchModel', 'moloni.api.CustomersGetByVatModel', 'moloni.api.CustomersGetLastNumberModel', 'moloni.api.CustomersGetModifiedSinceModel', 'moloni.api.CustomersGetOneModel', 'moloni.api.CustomersInsertModel', 'moloni.api.CustomersUpdateModel', 'moloni.api.DebitnotesClient', 'moloni.api.DebitnotesCountModel', 'moloni.api.DebitnotesDeleteModel', 'moloni.api.DebitnotesGetAllModel', 'moloni.api.DebitnotesGetOneModel', 'moloni.api.DebitnotesInsertModel', 'moloni.api.DebitnotesUpdateModel', 'moloni.api.DeductionsClient', 'moloni.api.DeductionsCountModifiedSinceModel', 'moloni.api.DeductionsDeleteModel', 'moloni.api.DeductionsGetAllModel', 'moloni.api.DeductionsGetModifiedSinceModel', 'moloni.api.DeductionsInsertModel', 'moloni.api.DeductionsUpdateModel', 'moloni.api.DeliverymethodsClient', 'moloni.api.DeliverymethodsCountModifiedSinceModel', 'moloni.api.DeliverymethodsDeleteModel', 'moloni.api.DeliverymethodsGetAllModel', 'moloni.api.DeliverymethodsGetModifiedSinceModel', 'moloni.api.DeliverymethodsInsertModel', 'moloni.api.DeliverymethodsUpdateModel', 'moloni.api.DeliverynotesClient', 'moloni.api.DeliverynotesCountModel', 'moloni.api.DeliverynotesDeleteModel', 'moloni.api.DeliverynotesGetAllModel', 'moloni.api.DeliverynotesGetOneModel', 'moloni.api.DeliverynotesInsertModel', 'moloni.api.DeliverynotesSetTransportCodeModel', 'moloni.api.DeliverynotesUpdateModel', 'moloni.api.DocumentmodelsClient', 'moloni.api.DocumentmodelsCountModifiedSinceModel', 'moloni.api.DocumentmodelsGetModifiedSinceModel', 'moloni.api.DocumentsClient', 'moloni.api.DocumentsCountModel', 'moloni.api.DocumentsGetAllDocumentTypesModel', 'moloni.api.DocumentsGetAllModel', 'moloni.api.DocumentsGetOneModel', 'moloni.api.DocumentsGetPdfLinkModel', 'moloni.api.DocumentsetsClient', 'moloni.api.DocumentsetsCountModifiedSinceModel', 'moloni.api.DocumentsetsDeleteModel', 'moloni.api.DocumentsetsGetAllModel', 'moloni.api.DocumentsetsGetModifiedSinceModel', 'moloni.api.DocumentsetsInsertModel', 'moloni.api.DocumentsetsUpdateModel', 'moloni.api.EstimatesClient', 'moloni.api.EstimatesCountModel', 'moloni.api.EstimatesDeleteModel', 'moloni.api.EstimatesGetAllModel', 'moloni.api.EstimatesGetOneModel', 'moloni.api.EstimatesInsertModel', 'moloni.api.EstimatesUpdateModel', 'moloni.api.FiscalzonesClient', 'moloni.api.FiscalzonesCountModifiedSinceModel', 'moloni.api.FiscalzonesGetAllModel', 'moloni.api.FiscalzonesGetModifiedSinceModel', 'moloni.api.IdentificationtemplatesClient', 'moloni.api.IdentificationtemplatesCountModifiedSinceModel', 'moloni.api.IdentificationtemplatesDeleteModel', 'moloni.api.IdentificationtemplatesGetAllModel', 'moloni.api.IdentificationtemplatesGetModifiedSinceModel', 'moloni.api.IdentificationtemplatesInsertModel', 'moloni.api.IdentificationtemplatesUpdateModel', 'moloni.api.InvoicereceiptsClient', 'moloni.api.InvoicereceiptsCountModel', 'moloni.api.InvoicereceiptsDeleteModel', 'moloni.api.InvoicereceiptsGetAllModel', 'moloni.api.InvoicereceiptsGetOneModel', 'moloni.api.InvoicereceiptsInsertModel', 'moloni.api.InvoicereceiptsUpdateModel', 'moloni.api.InvoicesClient', 'moloni.api.InvoicesCountModel', 'moloni.api.InvoicesDeleteModel', 'moloni.api.InvoicesGetAllModel', 'moloni.api.InvoicesGetOneModel', 'moloni.api.InvoicesInsertModel', 'moloni.api.InvoicesUpdateModel', 'moloni.api.LanguagesClient', 'moloni.api.LanguagesCountModifiedSinceModel', 'moloni.api.LanguagesGetModifiedSinceModel', 'moloni.api.MaturitydatesClient', 'moloni.api.MaturitydatesCountModifiedSinceModel', 'moloni.api.MaturitydatesDeleteModel', 'moloni.api.MaturitydatesGetAllModel', 'moloni.api.MaturitydatesGetModifiedSinceModel', 'moloni.api.MaturitydatesInsertModel', 'moloni.api.MaturitydatesUpdateModel', 'moloni.api.MeasurementunitsClient', 'moloni.api.MeasurementunitsCountModifiedSinceModel', 'moloni.api.MeasurementunitsDeleteModel', 'moloni.api.MeasurementunitsGetAllModel', 'moloni.api.MeasurementunitsGetModifiedSinceModel', 'moloni.api.MeasurementunitsInsertModel', 'moloni.api.MeasurementunitsUpdateModel', 'moloni.api.OwnassetsmovementguidesClient', 'moloni.api.OwnassetsmovementguidesCountModel', 'moloni.api.OwnassetsmovementguidesDeleteModel', 'moloni.api.OwnassetsmovementguidesGetAllModel', 'moloni.api.OwnassetsmovementguidesGetOneModel', 'moloni.api.OwnassetsmovementguidesInsertModel', 'moloni.api.OwnassetsmovementguidesSetTransportCodeModel', 'moloni.api.OwnassetsmovementguidesUpdateModel', 'moloni.api.PaymentmethodsClient', 'moloni.api.PaymentmethodsCountModifiedSinceModel', 'moloni.api.PaymentmethodsDeleteModel', 'moloni.api.PaymentmethodsGetAllModel', 'moloni.api.PaymentmethodsGetModifiedSinceModel', 'moloni.api.PaymentmethodsInsertModel', 'moloni.api.PaymentmethodsUpdateModel', 'moloni.api.ProductcategoriesClient', 'moloni.api.ProductcategoriesDeleteModel', 'moloni.api.ProductcategoriesGetAllModel', 'moloni.api.ProductcategoriesGetModifiedSinceModel', 'moloni.api.ProductcategoriesInsertModel', 'moloni.api.ProductcategoriesUpdateModel', 'moloni.api.ProductsClient', 'moloni.api.ProductsCountByEanModel', 'moloni.api.ProductsCountByNameModel', 'moloni.api.ProductsCountByReferenceModel', 'moloni.api.ProductsCountBySearchModel', 'moloni.api.ProductsCountModel', 'moloni.api.ProductsCountModifiedSinceModel', 'moloni.api.ProductsDeleteModel', 'moloni.api.ProductsGetAllModel', 'moloni.api.ProductsGetByEanModel', 'moloni.api.ProductsGetByNameModel', 'moloni.api.ProductsGetByReferenceModel', 'moloni.api.ProductsGetBySearchModel', 'moloni.api.ProductsGetModifiedSinceModel', 'moloni.api.ProductsGetOneModel', 'moloni.api.ProductsInsertModel', 'moloni.api.ProductsUpdateModel', 'moloni.api.ReceiptsClient', 'moloni.api.ReceiptsCountModel', 'moloni.api.ReceiptsDeleteModel', 'moloni.api.ReceiptsGetAllModel', 'moloni.api.ReceiptsGetOneModel', 'moloni.api.ReceiptsInsertModel', 'moloni.api.ReceiptsUpdateModel', 'moloni.api.SalesmenClient', 'moloni.api.SalesmenCountModifiedSinceModel', 'moloni.api.SalesmenDeleteModel', 'moloni.api.SalesmenGetAllModel', 'moloni.api.SalesmenGetModifiedSinceModel', 'moloni.api.SalesmenGetOneModel', 'moloni.api.SalesmenInsertModel', 'moloni.api.SalesmenUpdateModel', 'moloni.api.SimplifiedinvoicesClient', 'moloni.api.SimplifiedinvoicesCountModel', 'moloni.api.SimplifiedinvoicesDeleteModel', 'moloni.api.SimplifiedinvoicesGetAllModel', 'moloni.api.SimplifiedinvoicesGetOneModel', 'moloni.api.SimplifiedinvoicesInsertModel', 'moloni.api.SimplifiedinvoicesUpdateModel', 'moloni.api.SubscriptionClient', 'moloni.api.SubscriptionGetOneModel', 'moloni.api.SuppliersClient', 'moloni.api.SuppliersCountByNameModel', 'moloni.api.SuppliersCountByNumberModel', 'moloni.api.SuppliersCountBySearchModel', 'moloni.api.SuppliersCountByVatModel', 'moloni.api.SuppliersCountModel', 'moloni.api.SuppliersCountModifiedSinceModel', 'moloni.api.SuppliersDeleteModel', 'moloni.api.SuppliersGetAllModel', 'moloni.api.SuppliersGetByNameModel', 'moloni.api.SuppliersGetByNumberModel', 'moloni.api.SuppliersGetBySearchModel', 'moloni.api.SuppliersGetByVatModel', 'moloni.api.SuppliersGetModifiedSinceModel', 'moloni.api.SuppliersGetOneModel', 'moloni.api.SuppliersInsertModel', 'moloni.api.SuppliersUpdateModel', 'moloni.api.TaxesClient', 'moloni.api.TaxesCountModifiedSinceModel', 'moloni.api.TaxesDeleteModel', 'moloni.api.TaxesGetAllModel', 'moloni.api.TaxesGetModifiedSinceModel', 'moloni.api.TaxesInsertModel', 'moloni.api.TaxesUpdateModel', 'moloni.api.TaxexemptionsClient', 'moloni.api.TaxexemptionsCountModifiedSinceModel', 'moloni.api.TaxexemptionsGetModifiedSinceModel', 'moloni.api.UsersClient', 'moloni.api.UsersGetAllModel', 'moloni.api.VehiclesClient', 'moloni.api.VehiclesCountModifiedSinceModel', 'moloni.api.VehiclesDeleteModel', 'moloni.api.VehiclesGetAllModel', 'moloni.api.VehiclesGetModifiedSinceModel', 'moloni.api.VehiclesInsertModel', 'moloni.api.VehiclesUpdateModel', 'moloni.api.WarehousesClient', 'moloni.api.WarehousesCountModifiedSinceModel', 'moloni.api.WarehousesDeleteModel', 'moloni.api.WarehousesGetAllModel', 'moloni.api.WarehousesGetModifiedSinceModel', 'moloni.api.WarehousesInsertModel', 'moloni.api.WarehousesUpdateModel', 'moloni.api.WaybillsClient', 'moloni.api.WaybillsCountModel', 'moloni.api.WaybillsDeleteModel', 'moloni.api.WaybillsGetAllModel', 'moloni.api.WaybillsGetOneModel', 'moloni.api.WaybillsInsertModel', 'moloni.api.WaybillsSetTransportCodeModel', 'moloni.api.WaybillsUpdateModel', 'moloni.base.MoloniBaseClient', 'moloni.base.MoloniBaseUrl', 'moloni.base.endpoint', 'moloni.base.fill_query_params', 'moloni.base.validate_data', 'moloni.base.setup_logger', 'moloni.base.NoMoreRecords', 'moloni.base.ApiException', 'moloni.base.AuthConfig', 'moloni.base.ApiResponse'],
    url='https://github.com/saleweaver/python-moloni',
    license='MIT',
    author='Michael',
    author_email='michael@datastic.co',
    description='Python wrapper for the Moloni API'
)
